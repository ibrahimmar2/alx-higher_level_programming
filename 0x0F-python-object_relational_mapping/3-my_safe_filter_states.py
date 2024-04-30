#!/usr/bin/python3

"""
    A script that lists all states from the database hbtn_0e_0_usa
    starting with capital letter N
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

    sql = """SELECT * FROM states
        WHERE name LIKE BINARY = %s
        ORDER BY id ASC"""

    cursor.execute(sql, (sys.argv[4],))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
