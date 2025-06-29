#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
Usage: ./8-model_state_fetch_first.py <mysql_username>
        <mysql_password> <database_name>
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

    # Connect to MySQL
    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch only the first State, ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Display the result of "Nothing if the table is empty"
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
