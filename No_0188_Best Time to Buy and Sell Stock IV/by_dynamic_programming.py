'''

Description:

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.



Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

'''



# n : the length of input prices

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( n )


from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        
        # ------------------------------------------------------------------
        def max_profit_k_inf( prices ):
            
            # Solve max profit with k = ∞ in DP, with space optimization
            
            dp_not_hold, dp_hold = 0, -float('inf')
            
            for stock_price in prices:
                
                prev_not_hold, prev_hold = dp_not_hold, dp_hold
                
                dp_not_hold = max(prev_not_hold, prev_hold + stock_price )
                dp_hold = max(prev_hold, prev_not_hold - stock_price)
                
            return dp_not_hold
        
        # ------------------------------------------------------------------
        
        n = len(prices)
        
        if k > n // 2:
            
            # k is larger than threshold, in this case, it is the same as k = ∞
            return max_profit_k_inf( prices )
        
        else:
            
            # k is smaller than or equal to threshold, solve in DP with [k transactions][n stock prices]
            dp = [ [ 0 for _ in range(n) ] for _ in range(k+1) ]
            
            for i in range(1, k+1):
                
                local_max_profit = -prices[0]
                
                for j in range(1, n):
                    
                    dp[i][j] = max( dp[i][j-1], local_max_profit + prices[j] )
                    local_max_profit = max( local_max_profit, dp[i-1][j-1] - prices[j] )
            
            return dp[k][n-1]        



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxProfit( prices=[2,4,1], k = 2)
        self.assertEqual(result, 2)


    
    def test_case_2( self ):

        result = Solution().maxProfit( prices=[3,2,6,5,0,3], k = 2)
        self.assertEqual(result, 7)



if __name__ == '__main__':

    unittest.main()                