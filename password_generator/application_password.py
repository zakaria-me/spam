import os
import hashlib

def generate_key(password):
  salt = os.urandom(32)

  key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

  path = get_path()

  with (open(path, mode='bw')) as password_key:
    password_key.write(salt + key)

def verify_key(password):
  path = get_path()
  with (open(path, mode="rb")) as password_key:
    salt = password_key.read(32)
    key=password_key.read()
  key_of_provided_password= hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
  if key == key_of_provided_password:
    return True
  else:
    return False

def get_path():
  path = "password_generator/password_key.txt"
  return path

def password_is_in_existence():
  path = get_path()
  if(os.path.isfile(path)):
    return True
  else:
    return False