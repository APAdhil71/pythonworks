file_path="Errorhandling\\numbers.txt"
fr=open(file_path,"r")
lst=[]
for line in fr:
    line=line.rstrip("\n")
    try:
        num=int(line)
        lst.append(num)
    except Exception as e:
        continue
print(lst)

print(max(lst))
print(min(lst))
print(sum(lst))
number_count={num:lst.count(num)for num in lst}
max_value=max(number_count())


