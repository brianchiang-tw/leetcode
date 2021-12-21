from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        def trade(day_d):
            
            if day_d == 0:
			    # Hold on day_#0 = buy stock at the price of day_#0
                # Not-hold on day_#0 = doing nothing on day_#0
                return -prices[0], 0
            
            prev_hold, prev_not_hold = trade(day_d-1)
    
            cur_hold = max(prev_hold, -prices[day_d] )
            cur_not_hold = max(prev_not_hold, prev_hold + prices[day_d] )
            
            return cur_hold, cur_not_hold
        
        # -------------------------------------
        
        last_day = len(prices)-1
        
		# max profit must be in not-hold state
        return trade(last_day)[1]



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxProfit( [7,1,5,3,6,4] )
        self.assertEqual(result, 5)


    def test_case_2( self ):

        result = Solution().maxProfit( [7,6,4,3,1] )
        self.assertEqual(result, 0)        


if __name__ == '__main__':

    unittest.main()        