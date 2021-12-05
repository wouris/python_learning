import mysql.connector

mydb = ''

def db_connection_wPass():
   global mydb
   mydb = mysql.connector.connect(
         host="localhost",
         user="root",
         password="",
         database="pswds"
         )

def db_connection():
   global cursor
   global mydb
   mydb = mysql.connector.connect(
   host="localhost",    #ip address of database host
   user="root",         #user for auth
   password="",         #password for auth
   )
   cursor = mydb.cursor()

   try:
      cursor.execute("CREATE DATABASE pswds")
      print('Created DB for passwords')
   except:
         db_connection_wPass()

db_connection()
cursor = mydb.cursor()

try:
   cursor.execute("CREATE TABLE passwords (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), username VARCHAR(255), age INT, height INT, password VARCHAR(255))")
except:
   pass