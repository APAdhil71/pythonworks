class Fibonacci:
    def solution(self,number):
        p = 0
        c = 1
        print(p)
        print(c)
        for i in range(1,number): 
            n=p+c
            print(n)
            p=c
            c=n
instance=Fibonacci()
instance.solution(12)
