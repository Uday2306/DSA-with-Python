# Asteroid Collision
'''
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
'''
# Optimal Solution
class Solution:
    def asteriodCollision(self,asteriods):
        n = len(asteriods)
        stack = []
        num = 0
        for i in range(n):
            if asteriods[i] > 0:
                stack.append(asteriods[i])
            else:
                while len(stack) != 0 and stack[-1]> 0 and stack[-1] < abs(asteriods[i]):
                    stack.pop()
                if len(stack) != 0 and stack[-1] == abs(asteriod[i]):
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteriod[i])
                
        return stack

obj = Solution()
asteriod = [3,5,-6,2,-1,4]
print(obj.asteriodCollision(asteriod))

'''
Time: O(n) – each asteroid is pushed and popped at most once.
Space: O(n) in the worst case for the stack (when no collisions happen).
'''