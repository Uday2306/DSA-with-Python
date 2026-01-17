# Second Largest Optimal Solution:

class Second_array:
    def secone_largestElament(self,nums):
        n = len(nums)
        largest = float("-inf")
        s_largest = float("-inf")

        smallest = float("inf")
        s_smallest = float("inf")

        for i in range(0,n):
            # for sencond Largest Element
            if nums[i] > largest:
                s_largest = largest
                largest = nums[i]
            elif nums[i] > s_largest and nums[i] != largest:
                s_largest = nums[i]
            
            # For second Smallest Element
            if nums[i] < smallest:
                s_smallest = smallest
                smallest = nums[i]
            elif nums[i] < s_largest and nums[i] != smallest:
                s_smallest = nums[i]


        return [s_largest, s_smallest]

             

obj = Second_array()
print("Second largest element is: ",obj.secone_largestElament([11,22,32,123,1234,132,67]))