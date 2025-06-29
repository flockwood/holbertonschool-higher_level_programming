#!/usr/bin/python3
"""
Defines the City class mapped to the `cities` table in MySQL.
Usage: import City and Base from this module when defining your ORM.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
# We reuse the same Base registry you set up in model_state.py
from model_state import Base


class City(Base):
    """ORM mapping for the `cities` table."""
    __tablename__ = 'cities'

    # 1. Primary key column, auto-incrementing integer, not nullable
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # 2. Name column, up to 128 characters, not nullable
    name = Column(String(128), nullable=False)

    # 3. Foreign key column pointing to states.id, not nullable
    #    This enforces at the database level that every city
    # must link to an existing state.
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
