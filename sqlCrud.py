import mysql.connector
from mysql.connector import Error
from decouple import config
import Log 

database = mysql.connector.connect(host= config('host'),
                                        database=config('database'),
                                        user=config('user'),
                                        password=config('password'))

class Database:

    def createtable():
        '''
        Description : Functuion to create table in database
        '''
        try:
            mycursor=database.cursor()#cursor() method create a cursor object  
            mycursor.execute("create table student(roll INT,name VARCHAR(255), marks INT)")
        except Exception as e:
            Log.logging.error(e)
                  
    def insertRecord():
        '''
        Description : Functuion to insert records in table.
        '''
        try:  
             #Execute SQL Query to insert record  
            mycursor=database.cursor()
            mycursor.execute("insert into student values(1,'Ayur',80),(2,'Shubham',89),(3,'Anuj',90)")  
            database.commit() # Commit is used for your changes in the database  
            Log.logging.log('Record inserted successfully...')   
        except:  
            # rollback used for if any error   
            database.rollback()
        finally:  
            database.close()#Connection Close  
if __name__ == '__main__':
    choice = input('Choose your option = ')

    if choice == '1':
        createObj=Database
        createObj.createtable()
    elif choice == '2':
        createObj=Database
        createObj.insertRecord()

    else:
        print('Wrong choice, You are going exist.')
