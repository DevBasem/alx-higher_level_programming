#!/usr/bin/python3
"""Script that changes the name of a State object from
the database hbtn_0e_6_usa"""

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

    # Query the State with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State to "New Mexico"
    state_to_update.name = "New Mexico"

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()
