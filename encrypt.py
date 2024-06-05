from cryptography.fernet import Fernet
import os


class Encryptor:
    def __init__(self, key_path='secret.key'):
        self.key_path = key_path
        self.key = self._initialize_key()

    def _initialize_key(self):
        if not os.path.exists(self.key_path):
            return self._generate_key()
        return self._load_key()

    def _generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_path, 'wb') as key_file:
            key_file.write(key)
        return key

    def _load_key(self):
        with open(self.key_path, 'rb') as key_file:
            return key_file.read()

    def encrypt_data(self, data):
        f = Fernet(self.key)
        return f.encrypt(data)

    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
            encrypted_data = self.encrypt_data(file_data)
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)
            print(f"File '{file_path}' has been encrypted.")
        except Exception as e:
            print(f"Error encrypting file '{file_path}': {e}")

    def encrypt_files_in_directory(self, directory):
        try:
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    self.encrypt_file(file_path)
            print(f"All files in directory '{directory}' have been encrypted.")
        except Exception as e:
            print(f"Error encrypting files in directory '{directory}': {e}")
