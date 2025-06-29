#!/usr/bin/python3
"""
Prints the State object with the name
passed as argument from database hbtn_0e_6_usa.
Usage: ./10-model_state_my_get.py <mysql_username> <mysql_password>
        <database_name> <state_name>
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Grab credentials
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]

    # Connect to MySQL
    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch exactly one State by name (safe from injection)
    state = session.query(State).filter(State.name == search_name).first()

    # Display the id or "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
