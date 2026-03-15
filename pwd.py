import string
import secrets
import os
import pyperclip



def recieve_input():
    print('Welcome to the password generator!')
    number = int(input('Enter the number of characters you would like: '))
    return number

def check_validation(number):
    while True:
        if number < 5:
            print('The number of digits should be higher than 4!')
            number = int(input('Enter the number of characters you would like: '))
        else:
            break
    return number
def generate_password(number, lower_case, upper_case, symbols, digits, anonymous):
    pool = ''
    pool += secrets.choice(lower_case)
    pool += secrets.choice(upper_case)
    pool += secrets.choice(symbols)
    pool += secrets.choice(digits)
    pool += secrets.choice(anonymous)
    remaining_number = number - len(pool)
    if remaining_number > 0:
        all_characters = string.ascii_letters + string.digits +string.punctuation
        remain = [secrets.choice(all_characters) for _ in range(remaining_number)]
        pool += ''.join(remain)
        
    elif remaining_number == 0:
        password = pool
    
    pool_list = list(pool)
    secrets.SystemRandom().shuffle(pool_list)
    password = ''.join(pool_list)
    return password



def main():
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    symbols = string.punctuation
    digits = string.digits
    anonymous = 'Ll10o'
    number = recieve_input()
    number = check_validation(number)
    password = generate_password(number, lower_case, upper_case, symbols, digits, anonymous)
    pyperclip.copy(password)
    print('Copied to clip board!')
    print(f'Your password is {password}')


main()

