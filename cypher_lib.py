import string

low_chars = string.ascii_lowercase
alphabet = list(low_chars)
ascii_lower = [ord(x) for x in alphabet]

def atbash():
    print("-" * 20)
    userInput = str(input("Enter word that you want to cypher (with no spaces or numebers) : ".upper()))
    upOrLow = str(input("do you want the code to be Uppercase or lowercase: (Upper/Lower)"))
    if not userInput.isdigit() and userInput.isalpha():
        for char in userInput:
            shiftedDenary = (25 - (ord(char.upper()) - 65)) + 65
            if upOrLow.lower() == "upper":
                print(chr(shiftedDenary), end = " ")
            elif upOrLow.lower() == "lower":
                print(chr(shiftedDenary).lower(), end = " ")
            else:
                print("Pick a valid selector")
    else:
        print("You had an incorrect character in your input!")
    print("-" * 20)
    print()

