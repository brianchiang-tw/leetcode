from typing import List
from functools import lru_cache

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        
        @lru_cache(maxsize=None)
        def subArray_ending_at(i):

            ## base case
            if i == 0:
                return nums[0]

            ## general cases:
            # compute maximal value of subarray ending at index i
            return max(subArray_ending_at(i-1) + nums[i], nums[i])

        # --------------------------------------------
        return max( subArray_ending_at(i) for i in range( len(nums) ) )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().maxSubArray( nums=[-2,1,-3,4,-1,2,1,-5,4] )
        self.assertEqual(result, 6)
        return


    def test_case_2(self):

        result = Solution().maxSubArray( nums=[1] )
        self.assertEqual(result, 1)
        return

    def test_case_3(self):

        result = Solution().maxSubArray( nums=[5,4,-1,7,8] )
        self.assertEqual(result, 23)
        return


if __name__ == '__main__':

    unittest.main()