#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

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

    # Execute the query to select states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id"
    cursor.execute(query)

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
