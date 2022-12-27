#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
Arguments:
    mysql_username - username to connect the mySQL
    mysql passwd - password to connect the mySQL
    database_name - Name of the database
    state_to_search -Name of the state entered by the user
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_to_search = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name, charset="utf8")
    cur = db.cursor()
    statement = """SELECT cities.name
                 FROM cities, states
                 WHERE BINARY states.name = %s
                 AND cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    # The execute function requires one parameter, the sql query.
    cur.execute(statement, (state_to_search,))
    all_rows = cur.fetchall()
    print(", ".join(row[0] for row in all_rows))
    cur.close()
    db.close()
