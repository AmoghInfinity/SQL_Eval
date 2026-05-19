import json

with open("datasets/sql_questions.json", "r") as f:

    questions = json.load(f)

print(questions[0])