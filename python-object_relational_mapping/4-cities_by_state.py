#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <username> <password> <database>
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Command-line args
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Create cursor and execute exactly one query
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    # Fetch and print every row as a tuple
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
