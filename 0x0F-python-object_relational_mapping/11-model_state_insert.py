#!/usr/bin/python3
'''Adds a State object to a database.
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        pword = sys.argv[2]
        db_name = sys.argv[3]
        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
            user, pword, db_name
        )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        new_state = State(name='Louisiana')
        session.add(new_state)
        try:
            session.flush()
            session.refresh(new_state)
            if new_state.id is not None:
                print('{}'.format(new_state.id))
        except Exception:
            session.rollback()
        finally:
            session.commit()
