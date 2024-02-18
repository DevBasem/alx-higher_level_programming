#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""

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

    # Query all State objects and display the results
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
