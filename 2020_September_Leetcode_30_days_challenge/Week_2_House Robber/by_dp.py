'''

Description:

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.


             
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400

'''



from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        size = len(nums)
        value_dp = [ 0 for _ in range(size) ]
        
        if size == 0:
            # Empty list
            return 0
        
        elif size == 1:
            # Only one item
            return nums[0]
    
        else:
            # Initialization
            value_dp[0] = nums[0]
            value_dp[1] = max(nums[0], nums[1])

            # General case
            for i in range(2, size):
                value_dp[i] = max(value_dp[i-2] + nums[i], value_dp[i-1] )

            return value_dp[-1]


# n : the length of input list, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )


## Space Complexity: O( n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().rob( nums=[1,2,3,1] )
        self.assertEqual(result, 4)


    def test_case_2( self ):
    
        result = Solution().rob( nums=[2,7,9,3,1] )
        self.assertEqual(result, 12)        


    def test_case_3( self ):
        
        result = Solution().rob( nums=[2,7] )
        self.assertEqual(result, 7)          


    def test_case_4( self ):
        
        result = Solution().rob( nums=[2] )
        self.assertEqual(result, 2)                        


    def test_case_5( self ):
        
        result = Solution().rob( nums=[] )
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()            