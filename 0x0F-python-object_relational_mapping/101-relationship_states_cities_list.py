#!/usr/bin/python3
"""Lists all State objects, and corresponding City objects"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]

    # Database connection
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
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
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
