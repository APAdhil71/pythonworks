file_path="Errorhandling\\num.txt"
fr=open(file_path,"r")
number=[]
for line in fr:
    line=line.rstrip("\n")
    try:
        num=int(line)
        number.append(num)
    except Exception as e:
        continue
print(number) 
even=[even for even in number if even%2==0]
print(even)
count_even={c:even.count(c) for c in even}
print(count_even)