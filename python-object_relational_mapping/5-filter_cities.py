#!/usr/bin/python3
"""
Lists all cities of a given state in the database hbtn_0e_4_usa
Usage: ./5-filter_cities.py <username> <password>
        <database> <state_name>
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Grab args
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4].strip()

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )

    # Execute one safe, parameterized query
    cursor = db.cursor()
    sql = (
        "SELECT cities.id, cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(sql, (state_name,))

    # Extract and dedupe city names on ascending id order
    seen = set()
    cities = []
    for city_id, city_name in cursor.fetchall():
        if city_name not in seen:
            seen.add(city_name)
            cities.append(city_name)

    # Print as a comma-separated list
    print(", ".join(cities))

    # Clean up
    cursor.close()
    db.close()
