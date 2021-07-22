'''
@Author: Ayur Ninawe
@Date: 2021-07-22 21:00:30
@Last Modified by: Ayur Ninawe
@Last Modified time: 2021-07-22 21:00:30
@Title : Connecting database with python and initializing subquery.
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
    
    def create_subquery():
        """
        Description:
            function that returns the employee detail whose id matches in a subquery.
        """
        try:
            cursor = database_con.cursor()
            query ="SELECT FIRST_NAME, AGE, INCOME FROM EMPLOYEE WHERE CONTACT_ID IN (SELECT CONTACT_ID FROM EMPLOYEE);  "
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
    
    def comparison_operator_subquery():
        """
        Description:
            function that returns the employee detail whose income is more than 6000 using subquery..
        """
        try:
            cursor = database_con.cursor()
            query ="select * from EMPLOYEE where CONTACT_ID IN (select CONTACT_ID from EMPLOYEE where INCOME > 6000);"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
    def not_in_subquery():
        """
        Description:
            function that returns customer detail who does not belong to Los Angeles City using NOT IN.
        """
        try:
            cursor = database_con.cursor()
            query ="select CustomerName , City from Customers where City NOT IN (select City FROM Customers where City = 'LosAngalis');"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
    def exist_subquery():
        """
        Description:
            function to use EXISTS operator to find the name and occupation 
            of the customer who has placed at least one order
        """
        try:
            cursor = database_con.cursor()
            query ="SELECT name, occupation FROM customer   WHERE EXISTS (SELECT * FROM orders WHERE customer.cust_id = orders.cust_id)"
            cursor.execute(query)
            result = cursor.fetchall()
            Log.logging.debug(result)
        except Exception as e:
            Log.logging.error(e)
            
            
if __name__ == '__main__':
    subqueryObj = Database
    subqueryObj.create_subquery()
    subqueryObj.comparison_operator_subquery()
    subqueryObj.not_in_subquery()
    subqueryObj.exist_subquery()