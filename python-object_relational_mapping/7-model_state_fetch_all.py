#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql_username>
        <mysql_password> <database_name>
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Parse credentials and database name
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Build the engine and session factory
    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print each state in the format "id: name"
    for state in states:
        print(f"{state.id}: {state.name}")
