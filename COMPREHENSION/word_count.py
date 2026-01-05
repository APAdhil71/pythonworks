text="this is a python program for word count this program is simple"
words=text.split(" ")
print(words)
result={w:words.count(w) for w in words}
print(result)