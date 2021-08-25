import tkinter as tk
import password_generator.generate_password as g_p
import database.database as db

def display_one_username_password(username, password):
  new_label = tk.Label(display_frame, text=username + " " + password)
  new_label.pack()


def display_all_username_password():
  connection = db.connect()
  cursor = db.create_cursor(connection)
  # Retrieve the username passwords
  for row in cursor.execute("SELECT * FROM username_password"):
    new_label = tk.Label(display_frame, text=row)
    new_label.pack()

def print_password():
  global password 
  password = g_p.generate_password(character_set.get(), int(input_length.get()))
  frame_print_password = tk.Frame(password_length_frame, pady=20)
  frame_print_password.pack()
  label = tk.Label(frame_print_password, text="The password generated is: " + password)
  label.pack()
  close_button = tk.Button(frame_print_password, text="Clear generated password", command=frame_print_password.destroy)
  close_button.pack()

def submit():
  db.submit(username.get(), password)
  display_one_username_password(username.get(), password)

def gui_main():

  # Global Frame
  root = tk.Tk()
  frame = tk.Frame(root)
  frame.pack()
  root.title("Password Manager")
  
  # Character set Frame
  character_set_frame = tk.Frame(root, pady=20)
  character_set_frame.pack()
  label_character = tk.Label(character_set_frame, text="Select character set")
  label_character.pack()
  global character_set
  character_set = tk.IntVar() 
  letters = tk.Radiobutton(character_set_frame, text="Ascii Letters(lower and capital)", variable=character_set, value=1)
  letters_digits = tk.Radiobutton(character_set_frame, text="Letters and digits", variable=character_set, value=2)
  letters_digits_special = tk.Radiobutton(character_set_frame, text="Letters and digits and special characters", variable=character_set, value=3)
  letters.pack()
  letters_digits.pack()
  letters_digits_special.pack()
  
  # Password length Frame
  global password_length_frame
  password_length_frame = tk.Frame(root, pady=20)
  password_length_frame.pack()
  label_password = tk.Label(password_length_frame, text="Indicate the password length: must be greater than 7")
  label_password.pack()
  password_length = tk.IntVar() 
  global input_length
  input_length = tk.Entry(password_length_frame, textvariable=password_length)
  input_length.pack()
  
  # Username Frame
  username_frame = tk.Frame(root, pady=20)
  username_frame.pack()
  username_label = tk.Label(password_length_frame, text="Indicate the username :")
  username_label.pack()
  global username
  username = tk.StringVar() 
  input_username = tk.Entry(password_length_frame, textvariable=username)
  input_username.pack()
  
  # Button to validate
  generate_button = tk.Button(root, text="Generate password", command=print_password)
  generate_button.pack()
  
  
  # Button to submit
  submit_frame = tk.Frame(root, pady=20)
  submit_frame.pack()
  submit_button = tk.Button(submit_frame, text="Add record to Database", command=submit)
  submit_button.pack()
  
  # Window to display username and password
  global display_frame
  display_frame = tk.Frame(root, pady=20)
  display_frame.pack() 
  #display_label = tk.Label(display_frame, text="Username to password records: ")
  #display_label.pack()
  display_all_username_password()


  # Launch the frame
  root.mainloop()