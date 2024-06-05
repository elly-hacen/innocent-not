from cryptography.fernet import Fernet
import os

class Encryptor:
    def __init__(self, key_path='secret.key'):
        self.key_path = key_path
        self.key = self.generate_key()

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_path, 'wb') as key_file:
            key_file.write(key)
        return key

    def load_key(self):
        self.key = open(self.key_path, 'rb').read()

    def encrypt_data(self, data):
        f = Fernet(self.key)
        encrypted_data = f.encrypt(data)
        return encrypted_data

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.encrypt_data(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def encrypt_files_in_directory(self, directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                self.encrypt_file(file_path)
