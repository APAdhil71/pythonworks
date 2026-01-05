employees=[
    ["sam",34000,2],
    ["adhil",20000,1],
    ["messi",300000,10],
    ["neymar",200000,11]
]
srt_emp_exp=sorted(employees,key=lambda emp :emp[2])
print(srt_emp_exp)