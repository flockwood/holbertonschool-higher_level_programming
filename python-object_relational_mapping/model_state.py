#!/usr/bin/python3
"""
Defines the State class and creates the states table in MySQL.
Usage: ./model_state.py <mysql_username> <mysql_password> <database_name>
"""


import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# Base registry for all ORM classes
Base = declarative_base()


# State class mapped to the 'states' table
class State(Base):
    """ORM mapping for 'states' table."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Grab credentials from command line
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine connected to your local MySQL
    engine = create_engine(
        f"mysql+mysqldb://{user}:{passwd}"
        "@localhost:3306/"
        f"{db_name}",
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
