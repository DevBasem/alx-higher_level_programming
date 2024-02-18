#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name,
        charset="utf8"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select distinct cities of the specified state
    query = """
    SELECT GROUP_CONCAT(DISTINCT cities.name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch the result and display it
    result = cursor.fetchone()
    if result[0]:
        print(result[0])
    else:
        print()

    # Close cursor and database connection
    cursor.close()
    db.close()
