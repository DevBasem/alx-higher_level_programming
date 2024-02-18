#!/usr/bin/python3
"""Lists cities by state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    state_name = argv[4]
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name, ))
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))
    cur.close()
    conn.close()
