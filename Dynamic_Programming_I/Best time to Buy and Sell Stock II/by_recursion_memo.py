from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def trade(day_d):
            
            if day_d == 0:
                
                # Hold on day_#0 = buy stock at the price of day_#0
                # Not-hold on day_#0 = doing nothing on day_#0
                return - prices[day_d], 0
            
            prev_hold, prev_not_hold = trade(day_d-1)
            
            hold = max(prev_hold, prev_not_hold - prices[day_d] )
            not_hold = max(prev_not_hold, prev_hold + prices[day_d] )
            
            return hold, not_hold
        
        # --------------------------------------------------
        last_day= len(prices)-1
        
        # Max profit must come from not_hold state (i.e., no stock position) on last day
        return trade(last_day)[1]


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