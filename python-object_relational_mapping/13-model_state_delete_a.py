#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py <mysql_username>
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

    # Delete all State objects whose name contains 'a'
    session.query(State).filter(State.name.contains('a')).delete(
        synchronize_session='fetch'
    )

    session.commit()
    session.close()
