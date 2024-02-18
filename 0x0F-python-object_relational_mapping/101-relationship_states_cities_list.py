#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]

    # Create MySQL engine using SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name),
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve State and City information
    result = (
        session.query(State)
        .order_by(State.id)
        .all()
    )

    # Display results
    for state in result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # Close the session
    session.close()
