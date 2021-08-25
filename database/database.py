import sqlite3 as sql

def connect():
  connection = sql.connect('password_manager.db')
  return connection

def create_cursor(connection):
  cursor = connection.cursor()
  return cursor

def submit(username, password):
  # Create database or connect to one
  connection = connect() 
  
  # Create cursor: it does stuff to the database
  cursor = create_cursor(connection)

  # Insert into table
   
  cursor.execute("INSERT INTO username_password VALUES (:username, :password)",
  {
    'username': username,
    'password': password
  }
  )
  

  # Create table
  '''
  cursor.execute("""
  CREATE TABLE username_password (
    username text,
    password text
  );
  """)
  '''
  
  # Commit changes
  connection.commit()
  
  # Close connection
  connection.close()