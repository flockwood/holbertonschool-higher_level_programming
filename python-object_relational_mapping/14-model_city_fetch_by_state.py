#!/usr/bin/python3
"""
Lists all City objects from the databaase hbtn_0e_14_usa,
displaying them as "<state name>: (<city id>) <city name>".
Usage: ./14-model_city_fetch_by_state.py <mysql_username>
        <mysql_password> <database_name>
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
# to join cities back to their state names
from model_state import State


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Build the SQLAlchmemy engine and open a session
    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Print each as "<state name>: (<city id>) <city name>"
    for city, state in rows:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
