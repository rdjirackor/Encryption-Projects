from cryptography.fernet import Fernet
from File_Details import a
key=Fernet.generate_key()
cipher=Fernet(key)
input_file_path=a
print(a)