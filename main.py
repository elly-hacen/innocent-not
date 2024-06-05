from encrypt import Encryptor
from decrypt import Decryptor


def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Encrypt a message")
        print("2. Encrypt a file")
        print("3. Encrypt all files in a directory")
        print("4. Decrypt a message")
        print("5. Decrypt a file")
        print("6. Decrypt all files in a directory")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encryptor = Encryptor()
            encryptor.load_key()
            encrypted_message = encryptor.encrypt_data(message.encode())
            print(f"Encrypted Message: {encrypted_message.decode()}")

        elif choice == '2':
            file_path = input("Enter the file path to encrypt: ")
            encryptor = Encryptor()
            encryptor.load_key()
            encryptor.encrypt_file(file_path)
            print(f"File {file_path} has been encrypted.")

        elif choice == '3':
            directory_path = input("Enter the directory path to encrypt files: ")
            encryptor = Encryptor()
            encryptor.load_key()
            encryptor.encrypt_files_in_directory(directory_path)
            print(f"All files in {directory_path} have been encrypted.")

        elif choice == '4':
            encrypted_message = input("Enter the message to decrypt: ")
            decrypt = Decryptor()
            decrypted_message = decrypt.decrypt_data(encrypted_message.encode())
            print(f"Decrypted Message: {decrypted_message.decode()}")

        elif choice == '5':
            file_path = input("Enter the file path to decrypt: ")
            decrypt = Decryptor()
            decrypt.decrypt_file(file_path)
            print(f"File {file_path} has been decrypted.")

        elif choice == '6':
            directory_path = input("Enter the directory path to decrypt files: ")
            decrypt = Decryptor()
            decrypt.decrypt_files_in_directory(directory_path)
            print(f"All files in {directory_path} have been decrypted.")

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
