'''
@Author: Ayur Ninawe
@Date: 2021-07-20 20:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-20 20:00:30
@Title : Connecting database with python and performing aggrigate functions on tables.
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
    
    def count_func(self):
        """
        Description:
            This function will count the entries based on query.
        """
        try:
            cursor = database_con.cursor()
            query ="select count(name) from student"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
        finally:
            database_con.close()
            
    def sum_function(self):
        """
        Description:
            This function will give the sum of entries in particular column.
        """
        try:
            cursor = database_con.cursor()
            sum_query = "select sum(marks) as 'total_marks' from student"
            cursor.execute(sum_query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
        finally:
            database_con.close()
            
if __name__ == '__main__':
    aggregate = Database()
    aggregate.count_func()
    aggregate.sum_function()
    
    