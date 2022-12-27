#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa with a name starting with N
avoiding SQL injection
Arguments:
    mysql_username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    database_name - Name of the database
    name_to_search -
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    name_to_search = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name, charset="utf8")
    cur = db.cursor()
    statement = """SELECT *FROM states
    WHERE BINARY states.name = %s ORDER BY states.id ASC"""
    # The execute function requires one parameter, the sql query.
    cur.execute(statement, (name_to_search,))
    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)
    cur.close()
    db.close()
