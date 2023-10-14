import random

print("Ton mot de passe :")

caracteres = "abcdefghijklmnopqrstuvwxyz123456789!=:;,"

password = ''

for x in range(8):
    password += random.choice(caracteres)

print(password)