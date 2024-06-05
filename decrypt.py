from cryptography.fernet import Fernet
import os

class Decryptor:
    def __init__(self, key_path='secret.key'):
        self.key_path = key_path
        self.key = self._load_key()

    def _load_key(self):
        if not os.path.exists(self.key_path):
            raise FileNotFoundError(f"Key file '{self.key_path}' not found.")
        with open(self.key_path, 'rb') as key_file:
            return key_file.read()

    def decrypt_data(self, encrypted_data):
        f = Fernet(self.key)
        return f.decrypt(encrypted_data)

    def decrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = self.decrypt_data(encrypted_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)
            print(f"File '{file_path}' has been decrypted.")
        except Exception as e:
            print(f"Error decrypting file '{file_path}': {e}")

    def decrypt_files_in_directory(self, directory):
        try:
            for filename in os.listdir(directory):
                file_path = os.path.join(directory, filename)
                if os.path.isfile(file_path):
                    self.decrypt_file(file_path)
            print(f"All files in directory '{directory}' have been decrypted.")
        except Exception as e:
            print(f"Error decrypting files in directory '{directory}': {e}")
