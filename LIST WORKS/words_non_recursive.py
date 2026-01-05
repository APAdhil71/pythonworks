words=["hello","hai","hello","is"]
non_recursive=[]
for w in words:
    occ=words.count(w)
    if occ==1:
        non_recursive.append(w)
print(non_recursive)

