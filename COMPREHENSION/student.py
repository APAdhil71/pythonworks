student={"aju":92,"binu":76,"chandru":64}
result={k:"A" if v>=90 else "B" if  v>=70 else "C "for k,v in student.items()}
print(result)
