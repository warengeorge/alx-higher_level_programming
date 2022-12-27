#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico
Arguments:
    mysql_usr - username to connect the mySQL
    mysql psw - password to connect the mySQL
    db_name - Name of the database
 https://docs.sqlalchemy.org/en/13/orm/tutorial.html
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_usr = argv[1]
    mysql_pswd = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_usr, mysql_pswd, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result_state = session.query(State).filter_by(id=2).first()
    result_state.name = "New Mexico"
    session.commit()
