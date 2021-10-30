from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        size = len(cost)
        dp = [ 0 for _ in range(size)]
        
        # base case
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # general cases
        for stair in range(2, size):
            
            dp[stair] = min(dp[stair-1], dp[stair-2]) + cost[stair]
            
        
        return min(dp[size-1], dp[size-2])


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