class Solution:

    def tribonacci(self, n:int)->int:

        # Initialization
        dp = {0:0, 1:1, 2:1}
        
        # base case
        if n in dp:
            return dp[n]
        
        # general cases:
        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
            
        return dp[n]


import unittest

class Testing( unittest.TestCase):

    def test_case_1(self):

        result  = Solution().tribonacci(n=4)
        self.assertEqual(result, 4)
        return 

    def test_case_2(self):

        result  = Solution().tribonacci(n=25)
        self.assertEqual(result, 1389537)
        return 


if __name__ == '__main__':

    unittest.main()        