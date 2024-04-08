from cryptography.fernet import Fernet
from dotenv import load_dotenv
# genereate key
key = Fernet.generate_key()
print(key)
load_dotenv