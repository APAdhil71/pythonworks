def consonant_count(word):
    c_count=0
    VOWELS="aeiou"
    for ch in word:
        if ch not in VOWELS and ch.isalpha():
            c_count+=1
    return c_count
print(consonant_count("hello"))
print(consonant_count("hello765"))
