import sqlite3 as sql

def submit(username, password):
  # Create database or connect to one
  connection = sql.connect('password_manager.db')
  
  # Create cursor: it does stuff to the database
  cursor = connection.cursor()

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