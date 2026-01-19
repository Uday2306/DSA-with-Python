# Fruit Into Baskets
'''
Problem Statement: There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree.
The goal is to gather as much fruit as possible, adhering to the owner's stringent rules :

There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.
Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.
Once reaching a tree with fruit that cannot fit into any basket, stop.
Return the maximum number of fruits that can be picked.
'''
'''
Input :fruits = [1, 2, 1]
Output :3
Explanation : We will start from first tree.
The first tree produces the fruit of kind '1' and we will put that in the first basket.
The second tree produces the fruit of kind '2' and we will put that in the second basket.
The third tree produces the fruit of kind '1' and we have first basket that is already holding fruit of kind '1'. So we will put it in first basket.
Hence we were able to collect total of 3 fruits.


Input : fruits = [1, 2, 3, 2, 2]
Output : 4
Explanation : we will start from second tree.
The first basket contains fruits from second , fourth and fifth.
The second basket will contain fruit from third tree.
Hence we collected total of 4 fruits.
'''
# Brute force solution
'''class Solution:
    def fruitsIntoBasket(self,fruits):
        n = len(fruits)
        max_lenght = 0
        

        for i in range(0,n):
            my_set = set()
            for j in range(i,n):
                my_set.add(fruits[j])
                
                if len(my_set) > 2:
                    break
                
                max_lenght = max(max_lenght,(j - i + 1))
        return max_lenght
    
obj = Solution()
fruits = [1,2,3,2,2]
print(obj.fruitsIntoBasket(fruits))
'''
'''
Time and Space Complexity
Time: O(n^2)
Space: O(1) to O(2) for the set (bounded by 2 distinct types)
'''

# Optimal Solution
class Solution:
    def fruitsIntoBasket(self,fruits):
        n = len(fruits)
        max_lenght = 0
        left = 0
        right = 0
        my_dict = {}
        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right],0) + 1

            while len(my_dict) > 2:
                my_dict[fruits[left]] -= 1

                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1
            
            if len(my_dict) <= 2:
                max_lenght = max(max_lenght,(right - left + 1))
            right += 1
        return max_lenght
obj = Solution()
fruits = [1,2,3,2,2]
print(obj.fruitsIntoBasket(fruits))
'''
Time and Space Complexity
Time: O(n)
Space: O(1) (bounded by 2 types)
'''