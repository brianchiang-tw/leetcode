'''

Description:

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.



Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.



Example 3:

Input: nums = [0]
Output: 0
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

'''


from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        # key: index pair of covered range
        # value: maximized value of picking
        memo = {}
        
        # --------------------------------------------
        
        def helper(left, right):
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            if left > right:
                return 0
            
            elif left == right:
                return nums[left]
            
            take_i = helper(left, right-2) + nums[right]
            not_to_take_i = helper(left, right-1) + 0
            
            optimal = max(take_i, not_to_take_i)
            memo[(left, right)] = optimal
            return optimal
        
        # --------------------------------------------
        size = len(nums)
        
        # Handler for corner cases
        if size == 0:
            return 0
        
        elif size == 1:
            return nums[0]
        
        elif size == 2:
            return max(nums[0], nums[1])
			
        # Optimal maximized profit = max( Consider Head but Tail is excluded, or Consider Tail but Head is ecluded )
        return max( helper(0, size-2), helper(1, size-1))


# n : the length of nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of recursion with memoization, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in sapce is the storage for recursion, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().rob( nums=[2,3,2] )
        self.assertEqual(result, 3)


    def test_case_2( self ):

        result = Solution().rob( nums=[1,2,3,1] )
        self.assertEqual(result, 4)


    def test_case_3( self ):

        result = Solution().rob( nums=[0] )
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()        