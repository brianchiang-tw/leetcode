from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr):
        
            size = len(arr)
            
            # base case
            if size == 1:
                return arr[0]
            
            
            # initialization
            dp = {0:arr[0], 1: max(arr[0], arr[1])}
            
            
            # general cases
            for i in range(2, size):
                dp[i] = max( dp[i-2] + arr[i], dp[i-1] + 0)
            
            return dp[size-1]

        # ----------------------------------------
        
        if len(nums) == 1:
            # Quick response for corner case
            return nums[0]
        
        # general cases
        return max( helper(nums[:-1]), helper(nums[1:]) )



import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().rob( nums=[2, 3, 2] )
        self.assertEqual(result, 3)
        return


    def test_case_2(self):

        result = Solution().rob( nums=[1, 2, 3, 1] )
        self.assertEqual(result, 4)
        return    


if __name__ == '__main__':

    unittest.main()