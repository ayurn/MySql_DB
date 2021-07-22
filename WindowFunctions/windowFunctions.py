'''
@Author: Ayur Ninawe
@Date: 2021-07-22 18:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-22 18:00:30
@Title : Connecting database with python and use window functions.
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
    
    def using_over():
        """
        Description:
            function to create window function for total sale in year.
        """
        try:
            cursor = database_con.cursor()
            create_procedure_query ="SELECT fiscal_year, sales_employee,sale,SUM(sale) OVER (PARTITION BY fiscal_year) total_sale FROM sales;"
            cursor.execute(create_procedure_query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
if __name__ == '__main__':
    windowObj = Database
    windowObj.using_over()