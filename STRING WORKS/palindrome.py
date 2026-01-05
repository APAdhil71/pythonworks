def is_palindrome(word):
    word=word.casefold() #user put uppercase words it will print only in lowercase because the casefold() fun
    return word == word [::-1]
print(is_palindrome("RADAR"))