# num = int(input("enter a number"))
# if num == 0:
#     print ("the number is zero")
# else:
#     print ("the number is non zero")
def word_count(sentence):
    words = sentence.split()     # split by spaces
    return len(words)

text = "Python is very easy to learn"
print(word_count(text))
