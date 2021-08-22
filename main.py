import string, random

def set_characters_set(character_set_number):
  if character_set_number == 1:
    all_characters = string.ascii_letters
  elif character_set_number == 2:
    all_characters = string.ascii_letters + string.digits
  elif character_set_number == 3:
    all_characters = string.ascii_letters + string.digits + string.punctuation
  return all_characters

generated_password = ""

def set_password_length(password_length):
  password_length= input("What length do you want your password to be? ")
  if password_length.isdigit() and int(password_length) <= 8:
    print("The length must be greater than 8")
    exit()
  elif password_length.isdigit() == False:
    print("The length must be an integer")
    exit()
  else:
    password_length = int(password_length)
  return password_length

for i in range(set_password_length):
  random_int = random.randint(0, len(set_characters_set) -1)
  generated_password += set_characters_set[random_int]

print("Here is your generated password:")
print(generated_password)