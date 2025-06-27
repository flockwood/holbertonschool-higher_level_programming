#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Takes 3 arguments: mysql username, mysql password and database name
Uses MySQLdb module to connect to MySQL server on localhost at port 3306
Results sorted in ascending order by states.id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset='utf8mb4'
    )
    
    # Create cursor object
    cursor = db.cursor()
    
    # Execute query to get all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Print each result
    for row in results:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()