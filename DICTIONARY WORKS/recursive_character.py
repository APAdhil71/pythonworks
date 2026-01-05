word="a man a plan a canal panama"
wc={}
for ch in word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
for k,v in wc.items():
    if v>1 and k.isalpha():
        print(k)