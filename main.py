# Tim Le
def display_menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")

def encode(password):
    encoded = ''
    for digit in password:
        shifted = int(digit) + 3
        if shifted > 9:
            encoded += str(shifted - 10)
        else:
            encoded += str(shifted)
    return encoded

def decode(encoded):
    pass

def main():
    encoded = ''
    while True:    
        display_menu()
        option = int(input("Please enter an option: "))
        if option == 1: # Encode
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2: # Decode
            pass
        else:
            break

if __name__ == "__main__":
    main()