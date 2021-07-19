import mysql.connector
from mysql.connector import Error
from decouple import config
#from loggerfile import Log
#import loggerfile
import Log 

database = mysql.connector.connect(host= config('host'),
                                        database=config('database'),
                                        user=config('user'),
                                        password=config('password'))

class Database:

    def createtable():
        '''
        Describe : Functuion to create table in database
        '''
        try:
            mycursor=database.cursor()#cursor() method create a cursor object  
            mycursor.execute("create table student(roll INT,name VARCHAR(255), marks INT)")
        except Exception as e:
            Log.logging.error(e)
            
if __name__ == '__main__':
    Database.createtable()