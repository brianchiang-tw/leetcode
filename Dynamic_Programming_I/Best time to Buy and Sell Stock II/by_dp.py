from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
		# It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float('inf'), 0
        
        for stock_price in prices:
            
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            
			# either keep hold, or buy in stock today at stock price
            cur_hold = max( prev_hold, prev_not_hold - stock_price )
			
			# either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max( prev_not_hold, prev_hold + stock_price )
            
        # maximum profit must be in not-hold state
        return cur_not_hold if prices else 0


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxProfit( [7,1,5,3,6,4] )
        self.assertEqual(result, 7)


    def test_case_2( self ):

        result = Solution().maxProfit( [1,2,3,4,5] )
        self.assertEqual(result, 4)        


    def test_case_3( self ):

        result = Solution().maxProfit( [7,6,4,3,1] )
        self.assertEqual(result, 0)      


if __name__ == '__main__':

    unittest.main()                