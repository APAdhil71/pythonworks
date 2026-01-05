def is_palindrome(word):
    if word==word[::-1]:
        return True      #Q9 IS_PALANDROME
    else:
        return False
print(is_palindrome("madam"))
print(is_palindrome("hello"))