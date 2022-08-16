# these numbers will need adjustment based on your use case
p = 3
q = 11
n = p * q
phi = (p - 1) * (q - 1)
e = 3


def find_d(e, phi):
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return d


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(c, d, n):
    return pow(c, d, n)


def string_to_list(string):
    string = string.lower()
    string = list(string)
    return string


def list_to_int(list):
    for i in range(len(list)):
        if list[i] == ' ':
            list[i] = 32
        elif list[i] == '.':
            list[i] = 27
        elif list[i] == "'":
            list[i] = 28
        else:
            list[i] = ord(list[i]) - 96
    return list


def encrypt_list(list, e, n):
    for i in range(len(list)):
        list[i] = encrypt(list[i], e, n)
    return list


def decrypt_list(list, d, n):
    for i in range(len(list)):
        list[i] = decrypt(int(list[i]), d, n)
    return list


def list_to_string(list):
    string = ''
    for i in range(len(list)):
        if list[i] == 32:
            string += ' '
        elif list[i] == 27:
            string += '.'
        elif list[i] == 28:
            string += "'"
        else:
            string += chr(list[i] + 96)
    return string


def encrypt_string_to_list(string):
    string = string.replace('[', '')
    string = string.replace(']', '')
    string = string.replace(',', '')
    string = string.split()
    return string


def encrypt_message():
    input0 = input("Enter a string to encrypt: ")
    input0 = string_to_list(input0)
    input0 = list_to_int(input0)
    print("raw: ", input0)
    input0 = encrypt_list(input0, e, n)
    print("encrypted: ", input0)


def decrypt_message():
    d = find_d(e, phi)
    # input message to decrypt here with no special characters or punctuation, just numbers and spaces
    input1 = 'Input message to decrypt here.'
    input1 = encrypt_string_to_list(input1)
    input1 = decrypt_list(input1, d, n)
    input1 = list_to_string(input1)
    print(input1)


def main():
    while True:
        print("Welcome to the RSA encryption program!")
        print("Please select an option:")
        print("You have to manaully enter the message to be decrypted in line 88 of this code.")
        print("d = ", find_d(e, phi))
        input3 = input(
            "Enter 'e' to encrypt a message, 'd' to decrypt a message, or 'q' to quit: ")
        if input3 == 'e':
            encrypt_message()
        elif input3 == 'd':
            decrypt_message()
        elif input3 == 'q':
            break
        else:
            print("Invalid input.")
            main()


if __name__ == '__main__':
    main()
    print("Thank you for using the RSA encryption program!")
    print("Goodbye!")


