words=["program","python","profession","project","prison","proformance"]
#genarate new list contain word starting with pro
new_list=[]
for w in words:
    if w.startswith("pro"):
        w=new_list.append(w)
print(new_list)


#genarate new list contain words ending with on 
output=[w for w in words if w.endswith("on")]
print(output)