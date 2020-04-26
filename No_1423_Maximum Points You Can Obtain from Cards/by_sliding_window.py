'''

Description:

There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.



Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.



Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.



Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1.



Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 

Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length

'''



from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        size = len(cardPoints)
        left, right = k-1, size-1
        
        # Initial pick: take all k card from left hand side
        current_pick = sum(cardPoints[:k])
        max_point = current_pick
        
        # adjustment
        for _ in range(k):
            
            # left hand side discards one, and right hand side picks one more 
            current_pick += ( cardPoints[right] - cardPoints[left] )
            
            # update max point
            max_point = max(max_point, current_pick)
            
            # update card index for both sides in adjustment
            left, right = left-1, right-1
            
        return max_point



# k : the pick up size of cards

## Time Complexity: O( k )
#
# The overhead in time is the cost of sliding window maintainance, which is of O( k )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and temporary variable, which is of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'card_point_array k')

def test_bench():

    test_data = [
                    TestEntry( card_point_array = [1,2,3,4,5,6,1], k = 3),
                    TestEntry( card_point_array = [2,2,2], k = 2),
                    TestEntry( card_point_array = [9,7,7,9,7,7,9], k = 7),
                    TestEntry( card_point_array = [1,1000,1], k = 1),
                    TestEntry( card_point_array = [1,79,80,1,1,1,200,1], k = 3),
                ]

    # expected output:
    '''
    12
    4
    55
    1
    202
    '''


    for t in test_data:

        print( Solution().maxScore( cardPoints = t.card_point_array, k = t.k) )

    return



if __name__ == '__main__':

    test_bench()                