#!/usr/bin/python3
import MySQLdb
import sys

print("Arguments received:", sys.argv)
print("Number of args:", len(sys.argv))

if len(sys.argv) != 4:
    print("Error: Need exactly 3 arguments")
    sys.exit(1)

print("Trying to connect to MySQL...")
try:
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    print("Connected successfully!")
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    print(f"Found {len(rows)} rows")
    
    for row in rows:
        print(row)
    
    cur.close()
    db.close()
    print("Connection closed")
    
except Exception as e:
    print(f"Error: {e}")