from encrypt_msg import EncryptMsg

global_key = None


def menu():
    print("1. Create key")
    print("2. Set key")
    print("3. Encrypt message")
    print("4. Decrypt message")
    print("5. Exit")
    choice = input("Enter your choice: ")

    return choice


def menu_set_key():
    input_key = ""
    while True:
        input_key = input("Enter the key: ")
        if EncryptMsg.is_valid_key(input_key):
            print(f"Key set: {input_key}")
            break
        else:
            print("Invalid key")

    return input_key


def is_empty_key():
    return global_key is None


while True:
    choice = menu()
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice")
        continue

    if choice == "1":
        global_key = EncryptMsg.create_key()
        print(f"Key created: {global_key}")

    elif choice == "2":
        global_key = menu_set_key()

    elif choice == "3":
        if is_empty_key():
            print("Key not set")
            continue
        message = input("Enter the message: ")
        encrypted = EncryptMsg(global_key).encrypt(message)
        print(f"Encrypted message: {encrypted}")

    elif choice == "4":
        if is_empty_key():
            print("Key not set")
            continue

        message = input("Enter the encrypted message: ")
        decrypted = EncryptMsg(global_key).decrypt(message)
        print(f"Decrypted message: {decrypted}")

    elif choice == "5":
        print("Exiting...")
        break
