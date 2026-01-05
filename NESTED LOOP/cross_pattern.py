n = 5
mid = n // 2

for i in range(n):
    for j in range(n): #Q6
        if i == mid or j == mid:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
