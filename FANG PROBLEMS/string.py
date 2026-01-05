text = "Hello World"
word = "world"
result = word.lower() in text.lower()
print(result) 

sentence = "Python is easy to learn"
words = sentence.split()
print(len(words))  # 5

text = "programming"
ch = "g"
print(text.find(ch))     # first occurrence
print(text.rfind(ch))    # last occurrence

sentence = "python is fun"
result = sentence.title()
print(result)  # Python Is Fun

text = "hello world"
print(text.endswith("world"))  # True
print(text.endswith("d"))      # True

text = "Python Programming"
result = ""
for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch
print(result)  # Pyth*n Pr*gr*mm*ng

str1 = "listen"
str2 = "silent"
s1 = sorted(str1.lower())
s2 = sorted(str2.lower())
print(s1 == s2)  # True

email = "user@gmail.com"
username = email.split("@")[0]
print(username)  # user
