'''
@Author: Ayur Ninawe
@Date: 2021-07-20 14:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-20 14:00:30
@Title : Connecting database with python and performing aggrigate functions on tables.
'''
import mysql.connector
from mysql.connector import Error
from decouple import config
import Log 

database_con = mysql.connector.connect(host= config('HOST'),
                                        database=config('DATABASE'),
                                        user=config('USER'),
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
            Log.logging.info(result)
        except Exception as e:
            Log.logging.error(e)
        finally:
            database_con.close()
            
if __name__ == '__main__':
    aggregate = Database()
    aggregate.count_func()