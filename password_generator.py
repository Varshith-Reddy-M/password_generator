import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

n_l = int(input("Enter how many letters do you want in your password: "))
n_n = int(input("Enter how many numbers do you want in your password: "))
n_s = int(input("Enter how many symbols do you want in your password: "))
password = []
for i in range(n_l):
    password.append(random.choice(letters))
for i in range(n_n):
    password.append(random.choice(numbers))
for i in range(n_s):
    password.append(random.choice(symbols))
random.shuffle(password)
password = "".join(password)
print(f"Your password is: {password}")