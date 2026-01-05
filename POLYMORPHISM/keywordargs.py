def display_person(**kwargs):# **kwargs used for reciveing as dictionary
    print(kwargs)
display_person(name="hari",age=23,n_place="tvm",w_place="kakkanad",salary=34500)
def operation(*args,**kwargs):
    op=kwargs.get("key")
    if op=="max":
        return max(args)
    else:
        return min(args)
print(operation(10,20,30,key="max"))
print(operation(10,20,30,key="min"))