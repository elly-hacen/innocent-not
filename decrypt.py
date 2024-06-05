from cryptography.fernet import Fernet
import os


class Decryptor:
    def __init__(self, key_path='secret.key'):
        self.key_path = key_path
        self.key = None
        self.load_key()

    def load_key(self):
        self.key = open(self.key_path, 'rb').read()

    def decrypt_data(self, encrypted_data):
        f = Fernet(self.key)
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.decrypt_data(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

    def decrypt_files_in_directory(self, directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                self.decrypt_file(file_path)
