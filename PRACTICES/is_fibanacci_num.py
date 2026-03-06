class FibonacciNumber:
    def solution(self, number):
        is_fibonnaci_number = False
        p = 0
        c = 1
        n = 0

        while n <= number:
            if n == number:
                is_fibonnaci_number = True
                break  # stop the loop
            
            n = p + c
            p = c
            c = n

        return is_fibonnaci_number

instance = FibonacciNumber()
print(instance.solution(10))   # True
print(instance.solution(8))    # False
