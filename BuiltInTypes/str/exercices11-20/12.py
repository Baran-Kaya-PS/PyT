# Demande un mot et vérifie s’il est un palindrome.

user_input = input("--> ")


def palindrome(str):
    str = str.lower()
    if (str == str[::-1]):
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome(user_input)
