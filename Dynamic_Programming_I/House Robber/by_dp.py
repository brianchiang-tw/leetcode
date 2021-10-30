from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        size = len(nums)
        
        # base case
        if size == 1:
            return nums[0]
        
        
        # initialization
        dp = {0:nums[0], 1: max(nums[0], nums[1])}
        
        
        # general cases
        for i in range(2, size):
            dp[i] = max( dp[i-2] + nums[i], dp[i-1] + 0)
        
        return dp[size-1]


import unittest

class Testing( unittest.TestCase):

    def test_case_1(self):

        result = Solution().rob( nums=[1,2,3,1])
        self.assertEqual(result, 4)
        return 

    
    def test_case_2(self):

        result = Solution().rob( nums=[2,7,9,3,1])
        self.assertEqual(result, 12)
        return 


if __name__ == '__main__':
    unittest.main()