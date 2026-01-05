def count_vowels(words):
    vowels="aeiouAEIOU"
    count=0
    for char in words:      #Q10 COUNT VOWELS
        if char in vowels:
            count+=1
    return count
print(count_vowels("hello world"))