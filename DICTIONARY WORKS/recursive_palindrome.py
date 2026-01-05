words=["radar","mom","mom","dad","level","madam","dam","madam","malayalam","malayalam","madam"]
wc={}
for w in words:
    if w==w[::-1]:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
for k,v in wc.items():
    if v>1:
        print(k)