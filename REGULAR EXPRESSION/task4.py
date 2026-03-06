import re 
text="1 am in 5 days of indian tour"
pattern="[a-z]" # matches all lower case alphabet
print(re.findall(pattern,text))
text="i have 2 bike and 1 Car"
pattern="[A-Z]" # matches all lower case alphabet
print(re.findall(pattern,text))
text="i have 2 bike and 1 Car"
pattern="[A-Za-z]" # matches all both upper and lower case alphabet
print(re.findall(pattern,text))
text="i have 2 bike and 1 Car"
pattern="[0-9]" # matches all numbers
print(re.findall(pattern,text))
text="i have 2 bike and 1 Car"
pattern="[a-zA-Z0-9]" # matches all alphanumerical
print(re.findall(pattern,text))
text="i@ have# 2 bike and 1 Car#"
pattern="[^a-zA-Z0-9]" # matches all special characters
print(re.findall(pattern,text))
text="i@ have# 2 bike and 1 Car#"
pattern="[^a-zA-Z0-9 ]" # remove all special characters
print(re.sub(pattern,"",text))