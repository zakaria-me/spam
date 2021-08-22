import tkinter as tk
import generate_password as g_p

def print_password():
  generated_password = g_p.generate_password(character_set.get(), int(input_length.get()))
  frame_print_password = tk.Frame(root, pady=20)
  frame_print_password.pack()
  label = tk.Label(frame_print_password, text="The password generated is: " + generated_password)
  label.pack()
  close_button = tk.Button(frame_print_password, text="Clear generated password", command=frame_print_password.destroy)
  close_button.pack()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Password Generator")

# Character set Frame
character_set_frame = tk.Frame(root, pady=20)
character_set_frame.pack()
label_character = tk.Label(character_set_frame, text="Select character set")
label_character.pack()
character_set = tk.IntVar() 
letters = tk.Radiobutton(character_set_frame, text="Ascii Letters(lower and capital)", variable=character_set, value=1)
letters_digits = tk.Radiobutton(character_set_frame, text="Letters and digits", variable=character_set, value=2)
letters_digits_special = tk.Radiobutton(character_set_frame, text="Letters and digits and special characters", variable=character_set, value=3)
letters.pack()
letters_digits.pack()
letters_digits_special.pack()

# Password length Frame
password_length_frame = tk.Frame(root, pady=20)
password_length_frame.pack()
label_password = tk.Label(password_length_frame, text="Indicate the password length: must be greater than 7")
label_password.pack()
password_length = tk.IntVar() 
input_length = tk.Entry(password_length_frame, textvariable=password_length)
input_length.pack()

# Button to validate
generate_button = tk.Button(root, text="Generate password", command=print_password)
generate_button.pack()

# Launch the frame
root.mainloop()