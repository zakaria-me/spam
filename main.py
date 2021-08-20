import string, random

all_characters = string.ascii_letters + string.digits + string.punctuation
generated_password = ""

password_length= input("What length do you want your password to be? ")
if password_length.isdigit() and int(password_length) <= 8:
  print("The length must be greater than 8")
  exit()
elif password_length.isdigit() == False:
  print("The length must be an integer")
  exit()
else:
  password_length = int(password_length)

for i in range(password_length):
  random_int = random.randint(0, len(all_characters) -1)
  generated_password += all_characters[random_int]

print("Here is your generated password:")
print(generated_password)