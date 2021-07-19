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
    
    def displayRec():
        '''
        Description : Functuion to display records in table.
        '''
        try:  
            mycursor=database.cursor()
            mycursor.execute("select * from student")#Execute SQL Query to select all record   
            result=mycursor.fetchall() #fetches all the rows in a result set   
            for i in result:    
                roll=i[0]  
                name=i[1]  
                marks=i[2]  
                print(roll,name,marks)  
        except:   
            Log.logging.error('Error:Unable to fetch data.')
        finally:  
            database.close()#Connection Close  
    
    def updateRec():
        '''
        Description : Functuion to update records in table.
        '''
        try:  
            mycursor=database.cursor()
            mycursor.execute("UPDATE student SET name='Ramu', marks=100 WHERE roll=1")#Execute SQL Query to update record
            database.commit() # Commit is used for your changes in the database  
            print('Record updated successfully...')   
        except Exception as e:
            Log.logging.error(e)
        finally:    
            database.close()#Connection Close  
            
    def deleteRec():
        '''
        Description : Functuion to delete records in table.
        '''
        try:  
            mycursor=database.cursor()
            mycursor.execute("DELETE FROM student WHERE roll=3")#Execute SQL Query to update record
            database.commit() # Commit is used for your changes in the database  
            print('Record Deleted successfully...')   
        except Exception as e:
            Log.logging.error(e)
        finally:    
            database.close()#Connection Close  
                    
            
if __name__ == '__main__':
    print('Available Options: 1 : Create table, 2 : insert record, 3 : display records, 4 : update record 5 : delete record')
    choice = input('Choose your option = ')

    if choice == '1':
        createObj=Database
        createObj.createtable()
    elif choice == '2':
        createObj=Database
        createObj.insertRecord()
    elif choice == '3':
        createObj=Database
        createObj.displayRec()
    elif choice == '4':
        createObj=Database
        createObj.updateRec()
    elif choice == '5':
        createObj=Database
        createObj.deleteRec()
    
    else:
        print('Wrong choice, You are going exist.')
