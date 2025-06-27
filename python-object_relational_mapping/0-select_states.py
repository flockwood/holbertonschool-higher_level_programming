#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_user,
        passwd=mysql_passwd,
        db=mysql_db,
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to fetch all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all results
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
