from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Initialization
        memo = {0: cost[0], 1:cost[1]}

        def climb(n):
        
            # base case
            if n in memo:
                return memo[n]

            # general cases
            memo[n] = min(climb(n-1), climb(n-2)) + cost[n]
            return memo[n]
        
        # -------------------------------------------------
        n = len(cost)
        climb(n-1)
        return min( memo[n-1], memo[n-2] )


import unittest

class Testing( unittest.TestCase):

    def test_case_1(self):

        result = Solution().minCostClimbingStairs(cost=[10,15,20])
        self.assertEqual(result, 15)
        return


    def test_case_2(self):

        result = Solution().minCostClimbingStairs(cost=[1,100,1,1,1,100,1,1,100,1])
        self.assertEqual(result, 6)
        return        


if __name__ == '__main__':

    unittest.main()