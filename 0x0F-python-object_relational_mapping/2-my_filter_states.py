#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

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

    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY '{}'\
                    ORDER BY id ASC".format(sys.argv[4]))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
