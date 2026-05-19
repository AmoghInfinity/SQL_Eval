from evaluator.execute_sql import execute_query

query = "SELECT * FROM employees;"

result = execute_query(
    "database/company.db",
    query
)

print(result)