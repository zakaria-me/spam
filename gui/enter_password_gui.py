import tkinter as tk
from functools import partial
import password_generator.application_password as app_psswd
import gui.gui as gui 

def create_root_container():
  root = tk.Tk()
  root.title("Enter main password")
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
    pass
  else:
    # Inform of failure
    print("Failure")
    pass

def enter_passwd_frame():
  #global root
  root = create_root_container()
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

def enter_password_gui_main():
  # if psswd exists launch enter_psswd_frame
  if app_psswd.password_is_in_existence():
    enter_passwd_frame()
  else:
  # else launch the create psswd ? Which means new user, new database,...
    pass
  pass