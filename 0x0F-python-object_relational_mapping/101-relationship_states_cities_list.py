#!/usr/bin/python3
"""List all State objects and their corresponding City objects"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Take command line arguments for MySQL username, password, and database name
    username, password, db_name = argv[1], argv[2], argv[3]

    # Create MySQL engine using SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
        .format(username=username, password=password, db_name=db_name),
        pool_pre_ping=True
    )

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve State and City information
    result = (
        session.query(State)
        .order_by(State.id)
        .all()
    )

    # Display results with 4-space indentation
    for state in result:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))

    # Close the session
    session.close()
