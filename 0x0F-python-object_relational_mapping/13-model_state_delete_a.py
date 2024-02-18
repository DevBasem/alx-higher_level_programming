#!/usr/bin/python3
"""Script that deletes all State objects with a name
containing the letter a"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    # Connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete all State objects with a name containing the letter a
    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%'))\
        .all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()
