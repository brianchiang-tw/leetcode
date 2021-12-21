from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        def dp( i ):
            
            if i == 0:
                # Base case on index 0
                # min value, max value, max product are first value in array
                return nums[0], nums[0], nums[0]
            
            
            ## General cases
            
            prev_min, prev_max, prev_product = dp(i-1)
            
            # local max comes from product of two positive numbers, or product of two negative numbers
            candidate = [prev_min * nums[i], prev_max * nums[i], nums[i] ]
            cur_min = min( candidate )
            cur_max = max( candidate )
            product = max(prev_product, cur_max)
            
            return cur_min, cur_max, product
        
        # ----------------------------------------
        return dp( len(nums)-1 )[2]

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