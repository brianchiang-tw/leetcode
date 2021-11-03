from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        cur_hold, cur_not_hold = -float('inf'), 0

        for stock_price in prices:

            prev_hold, prev_not_hold = cur_hold, cur_not_hold

            # either keep in hold, or just buy today with stock price
            cur_hold = max(prev_hold, 0 - stock_price)

            # either keep in not holding, or just sell today with stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)


        # max profit must be in not-hold state
        return cur_not_hold if prices else 0



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