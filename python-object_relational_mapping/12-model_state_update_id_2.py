#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa.
Usage: ./12-model_state_update_id.py <mysql_username> <mysql_password>
        <database_name>
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

    # Retrieve the State with id = 2
    state = session.query(State).get(2)

    # If it exists, update its name and commit
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
