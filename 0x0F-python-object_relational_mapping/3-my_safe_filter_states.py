#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument, safe from MySQL injections.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_searched = sys.argv[4]

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

    # Use parameterized query to select states where name matches the argument
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name_searched,))

    # Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
