#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a
   from the database hbtn_0e_6_usa"""

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

    # Query State objects containing the letter 'a' and display the results
    result = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)

    for state in result:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
