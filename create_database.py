import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
      conn = sqlite3.connect(db_file)
      print(sqlite3.version)
      return conn
    except:
      return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = 'database.db'
 
    sql_create_files_table = """ CREATE TABLE IF NOT EXISTS files (
                                        name text PRIMARY KEY
                                    ); """
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create files table
        create_table(conn, sql_create_files_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
  main()