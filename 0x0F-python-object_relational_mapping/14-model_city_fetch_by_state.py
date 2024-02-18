#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    # Query all City objects and print the results
    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
