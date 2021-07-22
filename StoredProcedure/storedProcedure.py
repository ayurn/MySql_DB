'''
@Author: Ayur Ninawe
@Date: 2021-07-21 23:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-21 23:00:30
@Title : Connecting database with python and use stored procedure.
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
    
    def create_stored_procedure():
        """
        Description:
            function to create stored procedure.
        """
        try:
            cursor = database_con.cursor()
            create_procedure_query ="create procedure emp_info() begin select * from EMPLOYEE where INCOME > 6000; select * FROM EMPLOYEE; end"
            cursor.execute(create_procedure_query)
            Log.logging.debug("Stored procedure is created")
        except Exception as e:
            Log.logging.error(e)
            
if __name__ == '__main__':
    storedObj = Database
    storedObj.create_stored_procedure()