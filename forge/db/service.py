from forge.db.connection import get_connection


def list_tables():
    """
    Return all table names.
    """
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
    """)

    return [row[0] for row in cursor.fetchall()]


def describe_table(table_name: str):
    """
    Return schema information.
    """
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")

    return cursor.fetchall()


def execute_query(query: str):
    """
    Execute a SQL query.
    """
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(query)

    return cursor.fetchall()