from typing import List

class Solution():

    def canJump(self, nums: List[int]) -> bool:

        size = len(nums)
        destination = size-1

        # further coverage can reach from index i
        dp = [ 0 for _ in range(size)]

        # initialization
        dp[0] = nums[0]

        # update coverage in DP
        for i in range(1, size):

            if dp[i-1] < i:
                # cannot jump to current index from start index
                return False
            
            dp[i] = max(dp[i-1], i + nums[i])

            if dp[i] >= destination:
                # can jump to destination from start index
                return True
            
        return dp[destination-1] >= destination



import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().canJump( nums=[2,3,1,1,4] )
        self.assertEqual(result, True)
        return
    
    def test_case_2(self):

        result = Solution().canJump( nums=[3,2,1,0,4] )
        self.assertEqual(result, False)
        return


if __name__ == '__main__':

    unittest.main()