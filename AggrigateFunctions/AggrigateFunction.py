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
            function will count the entries based on query.
        """
        try:
            cursor = database_con.cursor()
            query ="select count(name) from student"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
    def sum_funct(self):
        """
        Description:
            function will give the sum of entries in particular column.
        """
        try:
            cursor = database_con.cursor()
            sum_query = "select sum(marks) as 'total_marks' from student"
            cursor.execute(sum_query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
            
    def avg_funct(self):
        """
        Description:
            function will give the average of entries in particular column.
        """
        try:
            cursor = database_con.cursor()
            avg_query = "select avg(marks) as 'average salary' from student"
            cursor.execute(avg_query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
            
    def min_funct(self):
        """
        Description:
            function will give the minimum value in particular column.
        """
        try:
            cursor = database_con.cursor()
            min_query = "select min(marks) as 'minimum marks' from student"
            cursor.execute(min_query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
            
    def max_funct(self):
        """
        Description:
            function will give the maximum value in particular column.
        """
        try:
            cursor = database_con.cursor()
            max_query = "select max(marks) as 'maximum marks' from student"
            cursor.execute(max_query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
            
    def get_first(self):
        """
        Description:
            function will give the first value in particular column.
        """
        try:
            cursor = database_con.cursor()
            first_query = "select marks from student limit 1"
            cursor.execute(first_query)
            result = cursor.fetchall()
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)

            
if __name__ == '__main__':
    aggregate = Database()
    aggregate.count_func()
    aggregate.sum_funct()
    aggregate.avg_funct()
    aggregate.min_funct()
    aggregate.max_funct()
    aggregate.get_first()
    
    