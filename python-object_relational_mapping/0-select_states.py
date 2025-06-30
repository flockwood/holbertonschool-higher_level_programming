#!/usr/bin/python3
"""
List all states from the database hbtn_0e_usa
Usage: ./0-select_states.py <username> <password> <database>
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Get credentials from command line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all rows
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
