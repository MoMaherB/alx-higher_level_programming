#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect(
    host="localhost",
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)
if __name__ == "__main__":
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
