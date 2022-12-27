#!/usr/bin/python3
"""
Python file that contains the class definition of a State
and an instance Base = declarative_base()
    https://docs.sqlalchemy.org/en/13/orm/tutorial.html
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Inherits from Base Tips and links to the MySQL table states"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
