def print_menu():
    print('Menu \n-------------\n1. Encode\n2. Decode\n3. Quit')

def encode(password_input): #123
    encoded_pass = ''
    for i in password_input:
        encoded_pass += str(int(i) + 3)
    return encoded_pass


'''def decode(password_input):
    decoded_pass = ''
    for i in password_input:
        decoded_pass += str(int(i) - 3)
    return decoded_pass'''


def main():
    keep_going = True
    while keep_going == True:
        print_menu()
        _option = int(input('Please enter an option:'))
        print('')
        if _option == 1:
            password_input = input('Please enter your password to encode:')
            encoded_pass = encode(password_input)
            print('Your password has been encoded and stored!')
            print('')

        elif _option == 2:
            decoded_pass = decode(encoded_pass)
            print('The encoded password is',encoded_pass,', and the original password is',decoded_pass)
        elif _option ==3:
            keep_going = False
            break




if __name__ == "__main__":
    main()




