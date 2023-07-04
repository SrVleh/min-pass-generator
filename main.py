import string, random

passSize = 0
enableSpecialChars = False
specialCharacters = '!@#$%^&*'


def setSpecialChars():
    while True:
        specialCharsResponse = input("Do you want to use special characters? y/n?")
        if specialCharsResponse == 'y':
            return True
        if specialCharsResponse == 'n':
            return False
        else:
            continue


def generatePassword():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(passSize))
    if enableSpecialChars:
        password = password[:-1] + random.choice(specialCharacters)

    return password


while True:
    try:
        passSize = int(input("Enter the password size:"))
        enableSpecialChars = setSpecialChars()
        break
    except ValueError:
        print("Please input integer only...")
        continue


print(generatePassword())
