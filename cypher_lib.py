
def atbash():
    print("-" * 20)
    userInput = str(input("Enter word that you want to cypher (with no spaces or numbers) : ".upper()))
    if not userInput.isalpha():
        print("You had an incorrect character in your input!")
        return False
    upOrLow = str(input("do you want the code to be Uppercase or lowercase: (Upper/Lower)"))
    if upOrLow.lower() != "upper" and upOrLow.lower() != "lower":
        print("You had an incorrect character in your input!")
        return False
    for char in userInput:
        shiftedDenary = (25 - (ord(char.upper()) - 65)) + 65
        if upOrLow.lower() == "upper":
           print(chr(shiftedDenary), end = " ")
           continue
        print(chr(shiftedDenary).lower(), end = " ")
    print()
    print("-" * 20)

def rot13():
    print("-" * 20)
    userInput = str(input("Enter your text or word: "))
    for char in userInput:
        if char == " ":
            print(" ", end = "")
        if char.isupper():
           print(chr((ord(char) - ord('A') + 13) % 26 + ord('A')), end = "")
        if char.islower():
            print(chr((ord(char) - ord('a') + 13) % 26 + ord('a')), end = "")
        else:
            print(char, end = "")
    print()
    print("-" * 20)

def ceaser():
    print("-" * 20)
    userInput = str(input("Enter your text or word: "))
    shift = int(input("Enter a what size of shift: ")) % 26
    for char in userInput:
        if char.isupper():
           print(chr((ord(char) - ord('A') + shift) % 26 + ord('A')), end = "")
        elif char.islower():
            print(chr((ord(char) - ord('a') + shift) % 26 + ord('a')), end = "")
        else:
            print(char, end = "")
    print()
    print("-" * 20)