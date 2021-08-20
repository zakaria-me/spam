import string, random

all_characters = string.ascii_letters + string.digits + string.punctuation
generated_password = ""

for i in range(0,7):
  random_int = random.randint(0, len(all_characters) -1)
  print(random_int)
  generated_password += all_characters[random_int]

print("Here is your generated password:")
print(generated_password)