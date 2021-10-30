class Solution:
    
    
    def climbStairs(self, n: int) -> int:    

        def method_count(n):
            
            # base case
            if n in memo:
                return memo[n]

            # general cases
            memo[n] = method_count(n-1) + method_count(n-2)
            return memo[n]

        # ----------------------------------

        memo = {0: 1, 1:1}
        return method_count(n)    


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