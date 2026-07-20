import sqlite3

_connection = None


def connect(database: str):
    """
    Connect to a SQLite database.
    """
    global _connection

    _connection = sqlite3.connect(database)

    return _connection


def get_connection():
    """
    Return the active database connection.
    """
    if _connection is None:
        raise RuntimeError("No database connected.")

    return _connection