'''
@Author: Ayur Ninawe
@Date: 2021-07-21 10:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-21 10:00:30
@Title : Connecting database with python and performing view operations on tables.
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
    
    def createView():
        """
        Description:
            function will create mysql view from given columns from table.
        """
        try:
            cursor = database_con.cursor()
            createView_query ="create view employee_info as select FIRST_NAME, INCOME from EMPLOYEE"
            cursor.execute(createView_query)
            Log.logging.debug('View created')
        except Exception as e:
            Log.logging.error(e)
            
    def displayView():
        """
        Description:
            function will display mysql view from given columns from table.
        """
        try:
            cursor = database_con.cursor()
            displayView_query =("select * from employee_info")
            cursor.execute(displayView_query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
            
if __name__ == '__main__':
    viewObj = Database
    viewObj.createView()
    viewObj.displayView()
    
