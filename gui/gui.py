import tkinter as tk
import password_generator.generate_password as g_p
import database.database as db

def display_one_username_password(username, password, url):
  new_label = tk.Label(display_username_frame, text=username)
  new_label.grid()
  new_label = tk.Label(display_password_frame, text=password)
  new_label.grid()
  new_label = tk.Label(display_url_frame, text=url)
  new_label.grid()

def display_all_username_password():
  connection = db.connect()
  cursor = db.create_cursor(connection)
  # Retrieve the username passwords
  cursor.execute("SELECT * FROM username_password")
  for row in cursor:
    new_label = tk.Label(display_username_frame, text=row[0])
    new_label.grid()
    new_label = tk.Label(display_password_frame, text=row[1])
    new_label.grid()
    new_label = tk.Label(display_url_frame, text=row[2])
    new_label.grid()

def print_password():
  global password 
  password = g_p.generate_password(character_set.get(), int(input_length.get()))
  frame_print_password = tk.Frame(password_length_frame, pady=20)
  frame_print_password.grid()
  label = tk.Label(frame_print_password, text="The password generated is: " + password)
  label.grid()
  close_button = tk.Button(frame_print_password, text="Clear generated password", command=frame_print_password.destroy)
  close_button.grid()

def submit():
  db.submit(username.get(), password, url.get())
  display_one_username_password(username.get(), password, url.get())

def gui_main():

  # Global Frame
  root = tk.Tk()
  frame = tk.Frame(root)
  frame.grid(row=0, column=0)
  root.title("Password Manager")
  
  # Character set Frame
  character_set_frame = tk.Frame(root, pady=20)
  character_set_frame.grid(row=0, column=0)
  label_character = tk.Label(character_set_frame, text="Select character set")
  label_character.grid(row=0, column=0)
  global character_set
  character_set = tk.IntVar() 
  letters = tk.Radiobutton(character_set_frame, text="Ascii Letters(lower and capital)", variable=character_set, value=1)
  letters_digits = tk.Radiobutton(character_set_frame, text="Letters and digits", variable=character_set, value=2)
  letters_digits_special = tk.Radiobutton(character_set_frame, text="Letters and digits and special characters", variable=character_set, value=3)
  letters.grid(row=1, column=0, sticky="nw")
  letters_digits.grid(row=2, column=0, sticky="nw")
  letters_digits_special.grid(row=3, column=0, sticky="nw")
  
  # Password length Frame
  global password_length_frame
  password_length_frame = tk.Frame(root)
  password_length_frame.grid(row=1, column=0)
  label_password = tk.Label(password_length_frame, text="Indicate the password length: must be greater than 7")
  label_password.grid(row=0, column=0)
  password_length = tk.IntVar() 
  global input_length
  input_length = tk.Entry(password_length_frame, textvariable=password_length)
  input_length.grid(row=1, column=0)
  # Username Frame
  username_frame = tk.Frame(root, pady=20)
  username_frame.grid(row=2, column=0)
  username_label = tk.Label(password_length_frame, text="Indicate the username :")
  username_label.grid(row=2, column=0)
  global username
  username = tk.StringVar() 
  input_username = tk.Entry(password_length_frame, textvariable=username)
  input_username.grid(row=3, column=0)
  # URL Frame
  url_frame = tk.Frame(root, pady=20)
  url_frame.grid(row=3, column=0)
  url_label = tk.Label(url_frame, text="Indicate the url :")
  url_label.grid(row=0, column=0)
  global url
  url = tk.StringVar() 
  input_url = tk.Entry(url_frame, textvariable=url)
  input_url.grid(row=1, column=0)
  # Button to validate
  generate_button = tk.Button(root, text="Generate password", command=print_password)
  generate_button.grid(row=4, column=0)
  
  
  # Button to submit
  submit_frame = tk.Frame(root, pady=20)
  submit_frame.grid(row=5, column=0)
  submit_button = tk.Button(submit_frame, text="Add record to Database", command=submit)
  submit_button.grid(row=0, column=0)
  
  # Window to display username and password
  global display_frame
  global display_username_frame
  global display_password_frame
  global display_url_frame
  display_frame = tk.Frame(root, pady=20, padx=20)
  display_frame.grid(row=0, column=1) 
  display_username_frame = tk.Frame(display_frame)
  display_username_frame.grid(row=1, column=0)
  display_password_frame = tk.Frame(display_frame)
  display_password_frame.grid(row=1, column=1)
  display_url_frame = tk.Frame(display_frame)
  display_url_frame.grid(row=1, column=2)
  table_username_label = tk.Label(display_username_frame, text="Username", pady=10)
  table_username_label.grid(row=0, column=0)
  table_password_label = tk.Label(display_password_frame, text="Password", pady=10)
  table_password_label.grid(row=0, column=0)
  table_url_label = tk.Label(display_url_frame, text="URL", pady=10)
  table_url_label.grid(row=0, column=0)
  display_all_username_password()
  
  # Launch the frame
  root.mainloop()