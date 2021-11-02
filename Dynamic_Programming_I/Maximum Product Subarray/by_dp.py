from typing import List

class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        global_max = prev_max = prev_min = nums[0]

        for number in nums[1:]:

            # local max comes from product of two positive numbers, or product of two negative numbers
            candidate = [prev_max * number, prev_min * number, number]
            local_max = max(candidate)
            local_min = min(candidate)

            # update global max
            global_max = max(global_max, local_max)

            prev_max, prev_min = local_max, local_min

        
        return global_max

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxProduct( nums=[2,3,-2,4] )
        self.assertEqual(result, 6)


    def test_case_2( self ):

        result = Solution().maxProduct( nums=[-2,0,-1] )
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()