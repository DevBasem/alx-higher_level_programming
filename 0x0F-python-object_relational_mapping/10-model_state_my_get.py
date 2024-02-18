#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
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

    # Query State object with the given name
    result = session.query(State).filter(State.name == argv[4]).first()

    if result:
        print(result.id)
    else:
        print("Not found")

    # Close the session
    session.close()
