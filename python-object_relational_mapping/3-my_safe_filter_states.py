#!/usr/bin/python3
"""
Safe filtering: displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed (protected from SQL injection)

Usage: ./3-my_safe_filter_states.py <username> <password>
        <database> <state_name>
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Grab credentials and raw state name
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    raw_state = sys.argv[4]
    state_name = raw_state.strip()

    # Connect to MySQL on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Create a cursor and execute a parameterized query
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql, (state_name,))

    # Fetch and print each matching row as a tuple
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
