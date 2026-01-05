lst=[4,10,11,12,14,16,9,7]
evens=list(filter(lambda n:n%2==0,lst))
print(evens)
odds=list(filter(lambda n:n%2!=0,lst))
print(odds)
num_gt_five=list(filter(lambda n:n>5,lst))
print(num_gt_five)