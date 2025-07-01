import os
from cryptography.fernet import Fernet

def list_files():
    files = []
    for file in os.listdir():
        if file.endswith(".py") or file.endswith(".key"):
            continue
        if os.path.isfile(file):
            files.append(file)
    return files

def encrypt_file(filename):
    key = Fernet.generate_key()
    with open(f"{filename}.key", "wb") as key_file:
        key_file.write(key)

    with open(filename, "rb") as f:
        contents = f.read()
    encrypted = Fernet(key).encrypt(contents)
    with open(filename, "wb") as f:
        f.write(encrypted)

    print(f"✅ Encrypted: {filename} (Key saved to {filename}.key)")

def decrypt_file(filename):
    key_file_path = f"{filename}.key"
    if not os.path.exists(key_file_path):
        print(f"❌ Key file not found for {filename}. Expected: {key_file_path}")
        return

    with open(key_file_path, "rb") as key_file:
        key = key_file.read()

    try:
        with open(filename, "rb") as f:
            contents = f.read()
        decrypted = Fernet(key).decrypt(contents)
        with open(filename, "wb") as f:
            f.write(decrypted)
        print(f"🔓 Decrypted: {filename}")
    except Exception as e:
        print(f"❌ Failed to decrypt {filename}: {e}")

def main():
    print("=== 🔐 File Encryption Tool ===")
    while True:
        print("\n1. List files")
        print("2. Encrypt a file")
        print("3. Decrypt a file")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            files = list_files()
            if files:
                for idx, f in enumerate(files):
                    print(f"{idx + 1}. {f}")
            else:
                print("No files available to show.")
        
        elif choice == "2":
            files = list_files()
            if not files:
                print("No files to encrypt.")
                continue
            for idx, f in enumerate(files):
                print(f"{idx + 1}. {f}")
            try:
                selection = int(input("Enter file number to encrypt: ")) - 1
                filename = files[selection]
            except (ValueError, IndexError):
                print("❌ Invalid selection.")
                continue

            encrypt_file(filename)

        elif choice == "3":
            files = list_files()
            if not files:
                print("No files to decrypt.")
                continue
            for idx, f in enumerate(files):
                print(f"{idx + 1}. {f}")
            try:
                selection = int(input("Enter file number to decrypt: ")) - 1
                filename = files[selection]
            except (ValueError, IndexError):
                print("❌ Invalid selection.")
                continue

            decrypt_file(filename)

        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid option. Choose between 1–4.")

if __name__ == "__main__":
    main()
