from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        global_max, local_max = nums[0], 0

        for number in nums:

            local_max = max(local_max + number, number)
            global_max = max(global_max, local_max)

        return global_max


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