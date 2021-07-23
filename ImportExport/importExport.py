'''
@Author: Ayur Ninawe
@Date: 2021-07-23 18:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-23 18:00:30
@Title : Connecting database with python and import, export database.
'''
import mysql.connector
from mysql.connector import Error
from decouple import config
import Log 
import os

database_con = mysql.connector.connect(host= config('HOST'),
                                        database=config('DATABASE'),
                                        user=config('DBUSER'),
                                        password=config('PASSWORD'))

class Database:
    
    def __init__(configuration):
        configuration.host = config('HOST')
        configuration.database=config('DATABASE')
        configuration.user=config('DBUSER')
        configuration.password=config('PASSWORD')
        

    def export_db(configuration,database_name,filename):
        '''
        Description : this function is to export database to .sql file
        
        Parameters: passing database name and file name for .sql
        '''
        try:
            os.system('mysqldump -u{} -p{} {} > {}.sql'.format(configuration.user,configuration.password,database_name,filename))
        except Exception as e:
            Log.logging.error(e)
            
def main():
    import_expObj = Database()
    database_name = 'sqlOperations'
    filename = 'expDB'
    
    try:
        import_expObj.export_db(database_name,filename)
    except Exception as e:
            Log.logging.error(e)

if __name__ == '__main__':
    main()

