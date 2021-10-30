class Solution:
    def fib(self, n: int) -> int:
        
        def getFib(n):
            
            ## base cases
            if n in memo:
                return memo[n]
            
            ## general cases
            memo[n] = getFib(n-1) + getFib(n-2)
            
            return memo[n]
        
        # ---------------------------------
        memo = {0:0, 1:1}
        
        return getFib(n)


import unittest

class Testing(unittest.TestCase):

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