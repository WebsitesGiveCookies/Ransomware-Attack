from cryptography.fernet import Fernet
from dotenv import load_dotenv
from os import getenv

# genereate key
# key = Fernet.generate_key()
load_dotenv()
key = getenv("KEY")
encryptor = Fernet(key=key.encode())
message = "message"
message = encryptor.encrypt(message.encode())
print(message)
