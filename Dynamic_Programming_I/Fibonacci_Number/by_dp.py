

class Solution:
    def fib(self, n: int) -> int:
        
        # initialization on boundary condition
        dp = {0: 0, 1:1}
        
        if n <= 1:
            
            # base case
            return dp[n]
        
        
        # general cases
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        n = 2
        result = Solution().fib( n=n )
        self.assertEqual(result, 1)


    def test_case_2( self ):
        n = 3
        result = Solution().fib( n=n )
        self.assertEqual(result, 2)

    def test_case_3( self ):
        n = 4
        result = Solution().fib( n=n )
        self.assertEqual(result, 3)        

    def test_case_3( self ):
        n = 10
        result = Solution().fib( n=n )
        self.assertEqual(result, 55)        


if __name__ == '__main__':

    unittest.main()               