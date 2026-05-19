import json
import pandas as pd
import time
import re

from models.ollama_client import generate_sql
from evaluator.execute_sql import execute_query
from evaluator.metrics import (
    execution_accuracy,
    valid_sql,
    exact_match
)

MODELS = [
    "qwen2.5-coder:7b",
    "deepseek-coder:6.7b",
    "mistral:7b"
]

DATABASE_PATH = "database/company.db"

SCHEMA = """
departments(dept_id, dept_name)

employees(emp_id, emp_name, age, salary, dept_id, joining_date)

projects(project_id, project_name, dept_id)

employee_projects(emp_id, project_id, hours_worked)
"""


def clean_sql_response(response_text):

    response_text = response_text.strip()

    response_text = re.sub(r"```sql", "", response_text)
    response_text = re.sub(r"```", "", response_text)

    response_text = response_text.strip()

    return response_text


with open("datasets/sql_questions.json", "r") as f:
    questions = json.load(f)

results = []

for model_name in MODELS:

    print("\n" + "=" * 60)
    print(f"Evaluating Model: {model_name}")
    print("=" * 60)

    for item in questions:

        question = item["question"]

        expected_sql = item["answer"]

        prompt = f"""
You are an SQL expert.

Database Schema:

{SCHEMA}

Question:
{question}

Generate ONLY SQL query.
Do not explain anything.
"""

        print("\nQuestion:")
        print(question)

        start_time = time.time()

        raw_response = generate_sql(
            model_name,
            prompt
        )

        latency = time.time() - start_time

        generated_sql = clean_sql_response(raw_response)

        print("\nGenerated SQL:")
        print(generated_sql)

        predicted_output = execute_query(
            DATABASE_PATH,
            generated_sql
        )

        expected_output = execute_query(
            DATABASE_PATH,
            expected_sql
        )

        is_execution_correct = execution_accuracy(
            predicted_output["result"],
            expected_output["result"]
        )

        is_valid_sql = valid_sql(
            predicted_output["success"]
        )

        is_exact_match = exact_match(
            generated_sql,
            expected_sql
        )

        results.append({
            "model": model_name,
            "question": question,
            "generated_sql": generated_sql,
            "expected_sql": expected_sql,
            "execution_correct": is_execution_correct,
            "valid_sql": is_valid_sql,
            "exact_match": is_exact_match,
            "latency_seconds": round(latency, 2)
        })

results_df = pd.DataFrame(results)

results_df.to_csv(
    "results/raw_outputs.csv",
    index=False
)

leaderboard = results_df.groupby("model").agg({
    "execution_correct": "mean",
    "valid_sql": "mean",
    "exact_match": "mean",
    "latency_seconds": "mean"
}).reset_index()

leaderboard["execution_correct"] = (
    leaderboard["execution_correct"] * 100
).round(2)

leaderboard["valid_sql"] = (
    leaderboard["valid_sql"] * 100
).round(2)

leaderboard["exact_match"] = (
    leaderboard["exact_match"] * 100
).round(2)

leaderboard["latency_seconds"] = (
    leaderboard["latency_seconds"]
).round(2)

leaderboard.rename(columns={
    "execution_correct": "execution_accuracy_percent",
    "valid_sql": "valid_sql_percent",
    "exact_match": "exact_match_percent",
    "latency_seconds": "avg_latency_seconds"
}, inplace=True)

leaderboard.to_csv(
    "results/leaderboard.csv",
    index=False
)

print("\n" + "=" * 60)
print("FINAL LEADERBOARD")
print("=" * 60)

print(leaderboard)