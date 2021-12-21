from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        def maxSubArray( A: List[int]) -> int:
        
            size = len(A)
            
            dp = [ 0 for _ in range(size)]
            dp[0] = A[0]

            for i in range(1, size):

                dp[i] = max(dp[i-1] + A[i], A[i])

            return max(dp)
        
        # -----------------------------------------------------------
        
        ## Boundary case, only one element
        if len(nums) == 1:
            return nums[0]
        
        ## General cases:
        
        # Maximal without first element
        drop = maxSubArray(nums[1:])
        
        # Maxiaml with first element selected
        pick = sum(nums) + max(0, maxSubArray([-number for number in nums[1:]]))
        
        return max(drop, pick)



import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().maxSubarraySumCircular( [1,-2,3,-2] )
        self.assertEqual(result, 3)


    def test_case_2(self):

        result = Solution().maxSubarraySumCircular( [5,-3,5] )
        self.assertEqual(result, 10)

    def test_case_3(self):

        result = Solution().maxSubarraySumCircular( [-3,-2,-3] )
        self.assertEqual(result, -2)


if __name__ == '__main__':

    unittest.main()