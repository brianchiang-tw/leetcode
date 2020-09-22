'''

Description:

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.


             
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''


from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # It is impossible to have stock to sell on first day, so -infinity is set as initial value
        init_hold, init_not_hold = -float('inf'), 0
        
        prev_hold, prev_not_hold = init_hold, init_not_hold
        
        for stock_price in prices:
            
            # either keep in hold, or just buy today with stock price
            cur_hold = max(prev_hold, -stock_price)
            
            # either keep in not holding, or just sell today with stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)
            
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
        
		# maximum profit must be in not-hold state
        return cur_not_hold if prices else 0


# n : the length of prices

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )

import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxProfit( prices=[7,1,5,3,6,4] )
        self.assertEqual(result, 5)


    def test_case_2( self ):

        result = Solution().maxProfit( prices=[7,6,4,3,1] )
        self.assertEqual(result, 0)

    

if __name__ == '__main__':

    unittest.main()