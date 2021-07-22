'''
@Author: Ayur Ninawe
@Date: 2021-07-22 21:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-22 21:00:30
@Title : Connecting database with python and initializing subquery.
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
    
    def create_subquery():
        """
        Description:
            function that returns the employee detail whose id matches in a subquery.
        """
        try:
            cursor = database_con.cursor()
            query ="SELECT FIRST_NAME, AGE, INCOME FROM EMPLOYEE WHERE CONTACT_ID IN (SELECT CONTACT_ID FROM EMPLOYEE);  "
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
if __name__ == '__main__':
    subqueryObj = Database
    subqueryObj.create_subquery()