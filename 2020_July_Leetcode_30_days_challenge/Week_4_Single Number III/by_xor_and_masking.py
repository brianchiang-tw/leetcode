'''

Description:

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

'''


from functools import reduce
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        xor = lambda x, y: x ^ y

        xor_result = reduce(xor, nums)

        # mask is the right-most 1 of xor result
        # use mask to separate nums into two groups, one group contains single_num_a, the other contains single_num_b
        mask = xor_result & -xor_result

        single_num_a, single_num_b = 0, 0

        for number in nums:
            # separate and collect these two single numbers by masking
            
            if number & mask:
                single_num_a ^= number
            
            else:
                single_num_b ^= number
        
        return [single_num_a, single_num_b]



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the cost of reduce and for loop iteration, which are of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage of loop index and bit manipulation, which are of O( 1 ).


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().singleNumber( nums = [1,2,1,3,2,5] )

        self.assertCountEqual(result, [3,5])



    def test_case_2( self ):
    
        result = Solution().singleNumber( nums = [1,1,2,2,3,4] )

        self.assertCountEqual(result, [3,4])


if __name__ == '__main__':

    unittest.main()