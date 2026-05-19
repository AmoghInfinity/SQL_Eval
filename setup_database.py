import sqlite3

conn = sqlite3.connect("database/company.db")

cursor = conn.cursor()

with open("database/schema.sql", "r") as f:
    schema_sql = f.read()

cursor.executescript(schema_sql)

with open("database/sample_data.sql", "r") as f:
    sample_data_sql = f.read()

cursor.executescript(sample_data_sql)

conn.commit()
conn.close()

print("Database setup completed successfully.")