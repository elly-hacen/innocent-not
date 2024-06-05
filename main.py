from rich import print
from rich.progress import Progress
from encrypt import Encryptor
from decrypt import Decryptor


def main():
    while True:
        print("\n[b blue]What would you like to do?[/b blue]")
        print("[1] Encrypt a message")
        print("[2] Encrypt a file")
        print("[3] Encrypt all files in a directory")
        print("[4] Decrypt a message")
        print("[5] Decrypt a file")
        print("[6] Decrypt all files in a directory")
        print("[7] Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            message = input("Enter the message to encrypt: ").strip()
            encryptor = Encryptor()
            encrypted_message = encryptor.encrypt_data(message.encode())
            print(f"[b green]Encrypted Message:[/b green] {encrypted_message.decode()}")

        elif choice == '2':
            file_path = input("Enter the file path to encrypt: ").strip()
            encryptor = Encryptor()
            encryptor.encrypt_file(file_path)

        elif choice == '3':
            directory_path = input("Enter the directory path to encrypt files: ").strip()
            encryptor = Encryptor()
            with Progress() as progress:
                task = progress.add_task("[green]Encrypting files...", total=1)
                encryptor.encrypt_files_in_directory(directory_path)
                progress.update(task, completed=1)
            print(f"[b green]All files in directory '{directory_path}' have been encrypted.[/b green]")

        elif choice == '4':
            encrypted_message = input("Enter the message to decrypt: ").strip()
            decryptor = Decryptor()
            try:
                decrypted_message = decryptor.decrypt_data(encrypted_message.encode())
                print(f"[b green]Decrypted Message:[/b green] {decrypted_message.decode()}")
            except Exception as e:
                print(f"[b red]Error decrypting message:[/b red] {e}")

        elif choice == '5':
            file_path = input("Enter the file path to decrypt: ").strip()
            decryptor = Decryptor()
            decryptor.decrypt_file(file_path)

        elif choice == '6':
            directory_path = input("Enter the directory path to decrypt files: ").strip()
            decryptor = Decryptor()
            with Progress() as progress:
                task = progress.add_task("[green]Decrypting files...", total=1)
                decryptor.decrypt_files_in_directory(directory_path)
                progress.update(task, completed=1)
            print(f"[b green]All files in directory '{directory_path}' have been decrypted.[/b green]")

        elif choice == '7':
            print("[b blue]Exiting...[/b blue]")
            break

        else:
            print("[b red]Invalid choice. Please enter a number between 1 and 7.[/b red]")


if __name__ == "__main__":
    main()
