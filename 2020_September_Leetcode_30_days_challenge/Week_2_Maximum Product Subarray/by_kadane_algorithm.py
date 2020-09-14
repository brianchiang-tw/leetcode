'''

Description:

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.



Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''


from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        global_max = prev_max = prev_min = nums[0]
        
        for number in nums[1:]:
            
            # local max comes from product of two positive numbers or product of two negative numbers
            local_max = max(prev_max * number, prev_min * number, number)
            local_min = min(prev_max * number, prev_min * number, number)
            
			# update global max
            global_max = max(global_max, local_max)
            
            prev_max, prev_min = local_max, local_min
            
        
        return global_max


# n : the length of input nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the stroage for loop index and temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxProduct( nums=[2,3,-2,4] )
        self.assertEqual(result, 6)


    def test_case_2( self ):

        result = Solution().maxProduct( nums=[-2,0,-1] )
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()
