class Solution:
    
    
    def climbStairs(self, n: int) -> int:    

        # base case
        dp = {0:1, 1:1}

        # general cases
        for i in range(2, n+1):

            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().climbStairs(n=2)
        self.assertEqual(result, 2)
        return


    def test_case_2(self):

        result = Solution().climbStairs(n=3)
        self.assertEqual(result, 3)
        return


    def test_case_3(self):

        result = Solution().climbStairs(n=10)
        self.assertEqual(result, 89)
        return


if __name__ == '__main__':

    unittest.main()