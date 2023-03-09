def print_menu():
    print('Menu \n-------------\n 1. Encode\n2. Decode\n3. Quit')

def encode(password_input):
    pass
def decode():
    pass

"""def main():
    #print menu



if __name__ == "__main__"
    main()"""

password_input = '12345555'
encoded_pass = ''
for i in password_input:
    encoded_pass += str(int(i) + 3)

print(encoded_pass)


