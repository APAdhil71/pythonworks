class ClosestNumberToZero:
    def solution(self,arr):
        closest_number=arr[0]
        for num in arr:
            if abs(num) <abs(closest_number):
                closest_number=num
        if closest_number<0 and abs(closest_number) in arr:
            return abs (closest_number)
        else:
            return closest_number
clst_instance=ClosestNumberToZero()
print(clst_instance.solution([-2,-3,2,3,4,-1]))

"""

class ClosestNumberToZero:
    def solution(self, arr):
        closest_number = arr[0]   # Start with the first element
        for num in arr:           # Loop through each number in the list
            if abs(num) < abs(closest_number):  
                # If the current number is closer to zero than the stored one
                closest_number = num

        # Special handling: if the closest number is negative
        # AND its positive counterpart also exists in the array
        if closest_number < 0 and abs(closest_number) in arr:
            return abs(closest_number)   # Return the positive version
        else:
            return closest_number
            
"""
