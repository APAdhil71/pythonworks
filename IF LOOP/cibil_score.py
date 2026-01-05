cibil_score = int(input("enter the cibil score"))
if cibil_score>=300 and cibil_score<550:
    print ("poor")
elif cibil_score>=550 and cibil_score<650:
    print("average")
elif cibil_score>=650 and cibil_score<700:
    print ("good")
elif cibil_score>=700 and cibil_score<900:
    print ("excellent")
else:
    print("invalid")