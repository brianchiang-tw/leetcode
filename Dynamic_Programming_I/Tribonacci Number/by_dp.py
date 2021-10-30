class Solution:

    def tribonacci(self, n:int)->int:

        def getTrib(n):
            
            ## base cases
            if n in memo:
                return memo[n]
            
            ## general cases
            memo[n] = getTrib(n-1) + getTrib(n-2) + getTrib(n-3)
            
            return memo[n]
        
        # ---------------------------------
        memo = {0:0, 1:1, 2:1}
        
        return getTrib(n)

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