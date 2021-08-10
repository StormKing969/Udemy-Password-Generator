import random
import string

def LetterGenerator(password_letter):
    letter = []
    for x in range(password_letter):
        letter += random.choice(string.ascii_letters)
    return letter


def NumberGenerator(password_number):
    num = []
    for x in range(password_number):
        num += str(random.randint(0, 9))
    return num


def SymbolGenerator(password_symbol):
    symbol = []
    for x in range(password_symbol):
        symbol += random.choice(string.punctuation)
    return symbol

def NewPassword(password_number, password_letter, password_symbol):
    output = NumberGenerator(password_number) + LetterGenerator(password_letter) + SymbolGenerator(password_symbol)
    random.shuffle(output)

    new_password = ""
    for i in output:
        new_password += i
    print(new_password)


if __name__ == '__main__':
    password_letter = int(input("How many letters do you want? "))
    password_number = int(input("How many numbers do you want? "))
    password_symbol = int(input("How many symbols do you want? "))

    NewPassword(password_number, password_letter, password_symbol)
