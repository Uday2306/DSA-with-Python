# Maximum Points You Can Obtain from Cards
'''
Problem Statement: Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.

Examples

Input :cardScore = [1, 2, 3, 4, 5, 6] , k = 3
Output : 15
Explanation :Choosing the rightmost cards will maximize your total score. 
So optimal cards chosen are the rightmost three cards 4 , 5 , 6.
Th score is 4 + 5 + 6 => 15.


Input :cardScore = [5, 4, 1, 8, 7, 1, 3 ] , k = 3
Output :12
Explanation : In first step we will choose card from beginning with score of 5.
In second step we will choose the card from beginning again with score of 4.
In third step we will choose the card from end with score of 3.
The total score is 5 + 4 + 3 => 12
'''
class Solution:
    def maxPointsObtained(self,cardPoints,k):
        if k == len(cardPoints):
                    return sum(cardPoints)

        max_sum = 0
        left_sum = 0
        right_sum = 0
        n = len(cardPoints)
        # Take all k from the left initially
        for i in range(k):
            left_sum += cardPoints[i]
        max_sum = left_sum

        # Slide: give back from left, take from right
        right_index = n - 1
        for i in range(k - 1, -1, -1):
            left_sum -= cardPoints[i]          # remove one from the left window
            right_sum += cardPoints[right_index]  # add one from the right tail
            right_index -= 1
            max_sum = max(max_sum, left_sum + right_sum)
        return max_sum

obj = Solution()
cardScore = [1,2,3,4,5,6,1]
k = 3

print(obj.maxPointsObtained(cardScore,k))
'''
Time:
Initial left sum: O(k)
Sliding k times: O(k)
Total: O(k) (plus O(1) checks), which is excellent when k ≤ n.
Space: O(1) – only a handful of variables.
'''