#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed
Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    raw_state = sys.argv[4]
    state_name = raw_state.strip()

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Create cursor and execute query (with.format() as required)
    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)
    cursor.execute(query)

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Close connection
    cursor.close()
    db.close()
