'''

Description:

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8

Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

'''


from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp_hold, dp_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = dp_hold, dp_not_hold
            
            # either keep not hold, or sell out today at stock price
            dp_not_hold = max(prev_not_hold, prev_hold + stock_price)
            
            # either keep hold, or buy in today at stock price and pay transaction fee for this trade
            dp_hold = max(prev_hold, prev_not_hold - stock_price - fee)
        
        # maximum profit must be in not-hold state
        return dp_not_hold if prices else 0



# n : the length of input prices

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the stroage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2)
        self.assertEqual(result, 8)



if __name__ == '__main__':

    unittest.main()