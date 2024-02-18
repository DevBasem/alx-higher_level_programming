#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects, contained in the
   database hbtn_0e_101_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]

    # Create the connection to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all states and their corresponding cities
    result = session.query(State).order_by(State.id).all()

    # Display the results
    for state in result:
        print(f"{state.id}: {state.name}")
        # Order the cities within each state by city id
        for city in sorted(state.cities, key=lambda x: x.id):
            print(f"    {city.id}: {city.name}")

    # Close the session
    session.close()
