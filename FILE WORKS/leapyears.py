file_path="C:\\Users\\adhil\\OneDrive\\Desktop\\pythonsworks\\while_loop\\for_loop\\nested_loop\\functions\\string_works\\list_works\\tuple_works\\set_works\\dictionary_works\\comprehension\\lambda_function\\file_works\\years.txt"
leap_years=[]
fr=open(file_path,"r")
for line in fr:
    year=int(line.rstrip("\n"))
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4!=0):
        leap_years.append(year)
print(leap_years)