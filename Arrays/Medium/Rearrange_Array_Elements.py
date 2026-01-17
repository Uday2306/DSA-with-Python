'''
Docstring for Medium.Rearrange_Array_Elements
###Rearrange Array Elements by Sign
Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
'''
'''
Example 1:
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
Explanation: 
Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.
'''
# Brute-Force Solution:
'''class Rearrange_Array_Elements:
    def rearrange_by_sign(self, A, n):
        pos = []  # List to hold positive numbers
        neg = []  # List to hold negative numbers

        # Step 1: Separate positives and negatives
        for i in range(n):
            if A[i] > 0:
                pos.append(A[i])
            else:
                neg.append(A[i])

        # Step 2: Place positives at even indices, negatives at odd indices
        for i in range(n // 2):
            A[2 * i] = pos[i]      # Even index → positive
            A[2 * i + 1] = neg[i]  # Odd index → negative

        return A

# Driver code
if __name__ == "__main__":
    A = [1, 2, -4, -5]
    n = len(A)

    obj = Rearrange_Array_Elements()
    result = obj.rearrange_by_sign(A, n)

    print(*result)  # Print result with space'''

# Optimal Solution
class Rearrange_Array_Elements:
    def arrayManipulation(self,nums):
        n = len(nums)
        result = [0] * n 
        pos,neg = 0 , 1
        for i in range(n):
            if  nums[i] > 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2
        
        return result

obj = Rearrange_Array_Elements()
nums = A = [1, 2, -4, -5]
print(obj.arrayManipulation(nums ))