text="hello world"
t={}
for ch in text:
    if ch in t:
        t[ch]+=1
    else:
        t[ch]=1
print(t)