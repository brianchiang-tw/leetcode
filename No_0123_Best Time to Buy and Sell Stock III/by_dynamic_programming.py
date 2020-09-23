'''

Description:

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.



Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.



Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.



Example 4:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105

'''



from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        dp_2_hold: max profit with 2 transactions, and in hold state
        dp_2_not_hold: max profit with 2 transactions, and not in hold state

        dp_1_hold: max profit with 1 transaction, and in hold state
        dp_1_not_hold: max profit with 1 transaction, and not in hold state

        Note: it is impossible to have stock in hand and sell on first day, therefore -infinity is set as initial profit value for hold state
        '''
        
        dp_2_hold, dp_2_not_hold = -float('inf'), 0
        dp_1_hold, dp_1_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
			# either keep being in not-hold state, or sell with stock price today
            dp_2_not_hold = max( dp_2_not_hold, dp_2_hold + stock_price )
			
			# either keep being in hold state, or just buy with stock price today ( add one more transaction )
            dp_2_hold = max( dp_2_hold, dp_1_not_hold - stock_price )
            
			# either keep being in not-hold state, or sell with stock price today
            dp_1_not_hold = max( dp_1_not_hold, dp_1_hold + stock_price )
			
			# either keep being in hold state, or just buy with stock price today ( add one more transaction )
            dp_1_hold = max( dp_1_hold, 0 - stock_price )
            
        
        return dp_2_not_hold


# n : the length of input prices

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        result = Solution().maxProfit( prices = [3,3,5,0,0,3,1,4] )
        self.assertEqual(result, 6)


    def test_case_2( self ):

        result = Solution().maxProfit( prices = [1,2,3,4,5] )
        self.assertEqual(result, 4)



if __name__ == '__main__':

    unittest.main()