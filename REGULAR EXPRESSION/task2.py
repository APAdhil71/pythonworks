import re 
text="i have 5 apple and i love eating apple"
print(len(re.findall("apple",text)))
print(re.sub("apple","orange",text))