#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name,
        charset="utf8"
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
