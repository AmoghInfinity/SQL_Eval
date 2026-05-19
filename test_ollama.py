from models.ollama_client import generate_sql

prompt = """
Database Schema:

employees(emp_id, emp_name, salary)

Question:
Retrieve all employees.

Generate ONLY SQL query.
"""

response = generate_sql(
    "qwen2.5-coder:7b",
    prompt
)

print(response)