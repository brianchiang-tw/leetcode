from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        dp = [ [0 for w in range(2)] for h in range(n) ]
        
        POSITIVE, NEGATIVE = 0, 1        
        
        if nums[0] > 0:
            dp[0][POSITIVE] = 1
            
        elif nums[0] < 0:
            dp[0][NEGATIVE] = 1
            
        
        max_len = dp[0][POSITIVE]
        
        for i in range(1, n):
            
            cur = nums[i]
            
            if cur > 0:
                dp[i][POSITIVE] = dp[i-1][POSITIVE] + 1
                
                if dp[i-1][NEGATIVE]:
                    dp[i][NEGATIVE] = max(dp[i][NEGATIVE], dp[i-1][NEGATIVE]+1 )
                    
            elif cur < 0:
                dp[i][NEGATIVE] = dp[i-1][POSITIVE] + 1
                
                if dp[i-1][NEGATIVE]:
                    dp[i][POSITIVE] = max(dp[i][POSITIVE], dp[i-1][NEGATIVE]+1 )
                    
            max_len = max(max_len, dp[i][POSITIVE])
            
        return max_len
                

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().getMaxLen([1,-2,-3,4])
        self.assertEqual(result, 4)


    def test_case_2( self ):

        result = Solution().getMaxLen([0,1,-2,-3,-4])
        self.assertEqual(result, 3)


if __name__ == '__main__':

    unittest.main()
