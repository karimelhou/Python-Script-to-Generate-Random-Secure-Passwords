import string
import random

# function to generate random passwords
def gen_pass(length):
    # generate random password
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    # check if the generated password meets the required criteria
    if not any(char.isdigit() for char in password):
        return gen_pass(length)
    elif not any(char.isupper() for char in password):
        return gen_pass(length)
    elif not any(char.islower() for char in password):
        return gen_pass(length)
    elif not any(char in string.punctuation for char in password):
        return gen_pass(length)
    else:
        return password

# function call
num = int(input('Enter the length of password to be generated: '))
print(gen_pass(num))