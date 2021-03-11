'''

Description:

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1



Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

'''



from typing import List

from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            # corner case for amount 0
            return 0
        
        # traversal queue
        # first parameter is current value
        # second paramter is step of coin change
        queue = deque([(0,0)])
        
        # set to record visited value
        visited = set([0])
        
        # BFS core
        while queue:
            
            cur, step = queue.popleft()
            
            for coin in coins:
                next_value = cur + coin
                
                if next_value == amount:
                    
                    # Accept, amount can be changed by coins
                    return step+1
                
                elif next_value <= amount and next_value not in visited:
                    queue.append( (next_value, step+1) )
                    visited.add( next_value )

        # Reject
        return -1


# n : the value of amount

## Time Complexity: O(  n )
#
# The overhead in time is the BFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for traversal queue, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().coinChange(coins = [1, 2, 5], amount = 11 )
        self.assertEqual(result, 3)


    def test_case_2(self):

        result = Solution().coinChange(coins = [2], amount = 3)
        self.assertEqual(result, -1)


    def test_case_3(self):

        result = Solution().coinChange(coins = [2], amount = 4)
        self.assertEqual(result, 2)        


    def test_case_4(self):

        result = Solution().coinChange(coins = [2], amount = 0)
        self.assertEqual(result, 0)  


    def test_case_5(self):

        result = Solution().coinChange(coins = [186,419,83,408], amount = 6249)
        self.assertEqual(result, 20)  

if __name__ == '__main__':

    unittest.main()