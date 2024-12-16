# /database/connection.py

import sqlite3

def get_db_connection():
    conn = sqlite3.connect("magazine.db")
    conn.row_factory = sqlite3.Row  # This will allow column names to be used like dictionary keys
    return conn
