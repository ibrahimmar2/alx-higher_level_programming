#!/usr/bin/python3

"""
    A script that lists all cities from the database hbtn_0e_0_usa
    Username, password and database names are given as user args
"""


import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    results = cursor.fetchall()

    tmp = list(row[0] for row in results)
    print(*tmp, sep=", ")

    cursor.close()
    db.close()
