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
            
    def display_index():
        """
        Description:
        function displays index in table employee.
        """
        try:
            cursor = database_con.cursor()
            query ="show indexes from EMPLOYEE;"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
            
    def explain_index():
        """
        Description:
        function to explain index in table employee.
        """
        try:
            cursor = database_con.cursor()
            query ="EXPLAIN SELECT * FROM EMPLOYEE WHERE CONTACT_ID = 101;"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
        
    def get_data_by_index():
        """
        Description:
        function to get data using index in table employee.
        """
        try:
            cursor = database_con.cursor()
            query ="SELECT * FROM EMPLOYEE WHERE CONTACT_ID = 103;"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
            
    def update_using_index():
        """
        Description:
        function to update data using index in table employee.
        """
        try:
            cursor = database_con.cursor()
            query ="UPDATE EMPLOYEE SET INCOME = 9000 WHERE CONTACT_ID = 103;"
            cursor.execute(query)
        except Exception as e:
            Log.logging.error(e)
            
    def drop_index():
        """
        Description:
        function to drop index in table employee.
        """
        try:
            cursor = database_con.cursor()
            query ="DROP INDEX EMP_ID ON EMPLOYEE"
            cursor.execute(query)
        except Exception as e:
            Log.logging.error(e)
            
if __name__ == '__main__':
    indexObj = Database
    indexObj.create_index()
    indexObj.display_index()
    indexObj.explain_index()
    indexObj.get_data_by_index()
    indexObj.update_using_index()
    indexObj.get_data_by_index()
    indexObj.drop_index()
    