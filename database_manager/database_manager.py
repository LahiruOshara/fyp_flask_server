import sys
sys.path.append('/')

import mysql.connector
from fyp_flask_server.database_manager import database_strings as dbstrings
from fyp_flask_server.database_manager import configurations



def create_db_connection():
    mydb = mysql.connector.connect(
        host=configurations.HOST,
        user=configurations.USER,
        passwd=configurations.PASSWORD,
        database=configurations.TWITTERDB,
        charset=configurations.CHARSET
    )
    # print("connection open")
    return mydb


def get_text_data(connection, data):
    if connection.is_connected():
        cursor = connection.cursor()

        try:
            cursor.execute(dbstrings.GET_SOLUTON.
                           format(data["EXTENSION"]))
            # connection.commit()
            return cursor.fetchall()
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            # reverting changes because of exception
            connection.rollback()

        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                # print("connection is closed")


# data = {'NAME': 'iaioauyfguyf', 'EXTENSION': 'khgahsd', 'SOLUTION': 'gkasgdkghas', 'TEXT': 'hahsldh'}
# store_text_data(create_db_connection(),data)
