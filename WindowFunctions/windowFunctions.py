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
            
    def cume_dist_func():
        """
        Description:
            function to use CUME_DIST function of window functions.
        """
        try:
            cursor = database_con.cursor()
            create_procedure_query ="SELECT name, score, ROW_NUMBER() OVER (ORDER BY score) row_num,CUME_DIST() OVER (ORDER BY score) cume_dist_val FROM scores;"
            cursor.execute(create_procedure_query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
    def dense_rank_func():
        """
        Description:
            function to use the DENSE_RANK() function to rank the sales employees by sale amount.
        """
        try:
            cursor = database_con.cursor()
            create_procedure_query ="SELECT sales_employee, fiscal_year, sale, DENSE_RANK() OVER (PARTITION BY fiscal_year ORDER BY sale DESC) sales_rank FROM sales;"
            cursor.execute(create_procedure_query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
        
    def first_value_func():
        """
        Description:
            function to use FIRST_VALUE() over the partition
        """
        try:
            cursor = database_con.cursor()
            create_procedure_query ="SELECT employee_name, department, hours, FIRST_VALUE(employee_name) OVER (PARTITION BY department ORDER BY hours) least_over_time FROM overtime;"
            cursor.execute(create_procedure_query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
        
if __name__ == '__main__':
    windowObj = Database
    windowObj.using_over()
    windowObj.cume_dist_func()
    windowObj.dense_rank_func()
    windowObj.first_value_func()