import psycopg2 as psql

def connect():
  connection = psql.connect("dbname=password_manager user=zakaria")
  return connection

def create_cursor(connection):
  cursor = connection.cursor()
  return cursor

def submit(username, password, url):
  # Create database or connect to one
  connection = connect() 
  
  # Create cursor: it does stuff to the database
  cursor = create_cursor(connection)

  # Insert into table
   
  cursor.execute("""INSERT INTO username_password VALUES (%s, %s, %s);""",
    (username, password, url)
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