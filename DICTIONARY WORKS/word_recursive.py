word="ABBAAACCAB"
wc={}
for ch in word:
    if ch in wc:
        print(ch,"the first recursive")
        break
    else:
        wc[ch]=1
    
