words=["hello","hai","hello","is"]
recursive=[]
for w in words:
    occ=words.count(w)
    if occ>1 and w not in recursive:
        recursive.append(w)
print(recursive)