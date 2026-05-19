import sqlite3


def execute_query(database_path, query):

    try:
        conn = sqlite3.connect(database_path)

        cursor = conn.cursor()

        cursor.execute(query)

        result = cursor.fetchall()

        conn.close()

        return {
            "success": True,
            "result": result,
            "error": None
        }

    except Exception as e:

        return {
            "success": False,
            "result": None,
            "error": str(e)
        }