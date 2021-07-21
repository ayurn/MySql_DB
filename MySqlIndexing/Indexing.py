'''
@Author: Ayur Ninawe
@Date: 2021-07-21 22:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-21 22:00:30
@Title : Connecting database with python and performing Indexing operations on tables.
'''
import mysql.connector
from mysql.connector import Error
from decouple import config
import Log 

database_con = mysql.connector.connect(host= config('HOST'),
                                        database=config('DATABASE'),
                                        user=config('DBUSER'),
                                        password=config('PASSWORD'))

class Database:
    
    def create_index():
        """
        Description:
        function cretaes index in table employee.
        """
        try:
            cursor = database_con.cursor()
            query ="CREATE UNIQUE INDEX EMP_ID ON EMPLOYEE (CONTACT_ID);"
            cursor.execute(query)
            Log.logging.info("Index created.")
        except Exception as e:
            Log.logging.error(e)
            
if __name__ == '__main__':
    indexObj = Database
    indexObj.create_index()