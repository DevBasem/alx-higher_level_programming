#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches
the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute the query to select states where name matches the argument
    query = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC
    """.format(argv[4])

    cur.execute(query)

    # Fetch all the rows and display them
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()
