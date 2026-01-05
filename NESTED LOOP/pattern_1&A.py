n = 4
for i in range(n):
    for j in range(n):
        if j <= i:    #Q7
            print(1, end=" ")
        else:
            print("A", end=" ")
    print()
