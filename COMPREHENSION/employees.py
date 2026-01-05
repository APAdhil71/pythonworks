empolyees=[
    {"id":200,"name":"adhil","email":"adhil71@gamil.com","salary":200000,"department":"hr"},
     {"id":2000,"name":"athul","email":"athul71@gamil.com","salary":60000,"department":"hr"},
     {"id":2001,"name":"bimal","email":"bimal71@gamil.com","salary":200000,"department":"hr"},
     {"id":2009,"name":"aahil","email":"aahil71@gamil.com","salary":90000,"department":"hr"}

]
#for d in empolyees:
   # print(d.get("name"))

#all_department={emp.get("department") for emp in empolyees}
#print(all_department)
#hr_employees=[e.get("name") for e in empolyees if e.get("department")=="hr"]
#print(hr_employees)

salary_empolyees=[e.get("name") for e in empolyees if e.get("salary")>20000]
print(salary_empolyees)
dc={}
for e in empolyees:
    dept=e.get("department")
    if dept in dc:
        dc[dept]+=1
    else:
        dc[dept]=1
print(dc)