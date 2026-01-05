treasure={"box1":"gold",
          "box2":"silver",
          "box3":"daimond",
          "box4":"paltinum"
}

#print(treasure["box3"])


#how can we add a key value pair of box5 iron
treasure["box5"]="iron"
#print(treasure)


#chk box6 exist if not add box6 with value copper

if "box6" not in treasure:
    treasure["box6"]="copper"
#print(treasure)

#iteration dictionary 
for k in treasure:
    print(k,treasure[k])


for k in treasure:
    print(k)


for k in treasure.keys():
    print("key=",k)
for v in treasure.values():
    print("values",v)
for v,k in treasure.items():
    print(k,v)

"""
def key() return keys
def value()return values
def items()return both values and keys
def get(item)
def pop()removing a specific key
"""


print(treasure.get("box100","empty box"))
print("task1")
print("task2")

treasure.pop("box2")
print(treasure)