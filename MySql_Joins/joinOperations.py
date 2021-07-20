'''
@Author: Ayur Ninawe
@Date: 2021-07-20 22:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-20 22:00:30
@Title : Connecting database with python and performing join operations on tables.
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
    
    def inner_join():
        """
        Description:
            function retrieves data from the two tables combined by 
            contact column of the EMPLOYEE table and ID column of the CONTACT table.
        """
        try:
            cursor = database_con.cursor()
            query ="SELECT * from EMPLOYEE INNER JOIN CONTACT ON EMPLOYEE.CONTACT = CONTACT.ID;"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
    def left_join():
        """
        Description:
            function retrieves data from the two tables and performs left join on them.
        """
        try:
            cursor = database_con.cursor()
            query ="SELECT * from EMPLOYEE LEFT JOIN CONTACT ON EMPLOYEE.CONTACT = CONTACT.ID;"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
    def right_join():
        """
        Description:
            function retrieves data from the two tables and performs right join on them.
        """
        try:
            cursor = database_con.cursor()
            query ="SELECT * from EMPLOYEE RIGHT JOIN CONTACT ON EMPLOYEE.CONTACT = CONTACT.ID;"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
    
            
if __name__ == '__main__':
    joins = Database
    joins.inner_join()
    joins.left_join()
    joins.right_join()