#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the
database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py <mysql_username>
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

    # Query only states whose name contains 'a', ordered by id
    states = (
        session.query(State)
        .filter(State.name.contains('a'))
        .order_by(State.id)
        .all()
    )

    # Print each matching state as "id: name"
    for state in states:
        print(f"{state.id}: {state.name}")
