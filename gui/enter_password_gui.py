import tkinter as tk
from functools import partial
import password_generator.application_password as app_psswd
import gui.gui as gui 

def create_root_container(title: str):
  root = tk.Tk()
  root.title(title)
  return root

def create_main_frame(parent):
  frame = tk.Frame(parent)
  return frame

def position_element(element):
  element.pack()

def enter_password(root):
  result = app_psswd.verify_key(password.get())
  if result == True:
    root.destroy()
    gui.gui_main()
  else:
    # Inform of failure
    print("Failure")
    pass

def enter_choice(root):
  if choice.get() == "change_password":
    root.destroy()
    change_password_frame()
  elif choice.get() == "enter_password":
    root.destroy()
    enter_passwd_frame()
  elif choice.get() == "set_password":
    root.destroy()
    set_password_frame()

def change_password(root):
  if app_psswd.verify_key(previous_password.get()):
    app_psswd.generate_key(new_password.get())
  else:
    print("Democracy in action ain't pretty!")
  root.destroy()
  welcome_frame()

def set_password(root):
  app_psswd.generate_key(new_password.get())
  root.destroy()
  welcome_frame()

def enter_passwd_frame():
  #global root
  root = create_root_container("Enter main password")
  main_frame = create_main_frame(root) 
  position_element(main_frame)
  label_password = tk.Label(main_frame, text="Type in your password")
  position_element(label_password)
  global password
  password = tk.StringVar() 
  input_password = tk.Entry(main_frame, textvariable=password)
  position_element(input_password)
  enter_password_button = tk.Button(root, text="Enter", command=partial(enter_password, root))
  position_element(enter_password_button)
  root.mainloop()

def change_password_frame():
  root = create_root_container("Time to change your password!")
  frame = create_main_frame(root)
  position_element(frame)
  previous_password_label = tk.Label(frame, text="Type in your previous password")
  position_element(previous_password_label)
  global previous_password
  previous_password = tk.StringVar()
  previous_password_entry = tk.Entry(frame, textvariable=previous_password)
  position_element(previous_password_entry)
  new_password_label = tk.Label(frame, text="Type in your new password")
  position_element(new_password_label)
  global new_password
  new_password = tk.StringVar()
  new_password_entry = tk.Entry(frame, textvariable=new_password)
  position_element(new_password_entry)
  change_password_button = tk.Button(frame, text="Change your password", command=partial(change_password, root))
  position_element(change_password_button)
  root.mainloop()

def set_password_frame():
  root = create_root_container("Time to change your password!")
  frame = create_main_frame(root)
  position_element(frame)
  new_password_label = tk.Label(frame, text="Type in your new password")
  position_element(new_password_label)
  global new_password
  new_password = tk.StringVar()
  new_password_entry = tk.Entry(frame, textvariable=new_password)
  position_element(new_password_entry)
  set_password_button = tk.Button(frame, text="Set your password", command=partial(set_password, root))
  position_element(set_password_button)
  root.mainloop()

def welcome_frame():
  root = create_root_container("Welcome to the app")
  frame = create_main_frame(root)
  position_element(frame)
  global choice
  choice = tk.StringVar()
  if app_psswd.password_is_in_existence():
    change_password = tk.Radiobutton(frame, text="Change your password", variable=choice, value="change_password")
    enter_password = tk.Radiobutton(frame, text="Enter your password", variable=choice, value="enter_password")
    position_element(change_password)
    position_element(enter_password)
  else:
    set_password = tk.Radiobutton(frame, text="Set your password", variable=choice, value="set_password")
    position_element(set_password)
  choose_button = tk.Button(frame, text=" Enter", command=partial(enter_choice, root))
  position_element(choose_button)
  root.mainloop()