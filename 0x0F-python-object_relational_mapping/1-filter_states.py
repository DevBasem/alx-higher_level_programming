#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    # Execute the query to select distinct states starting with 'N'
    cursor.execute("SELECT DISTINCT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
