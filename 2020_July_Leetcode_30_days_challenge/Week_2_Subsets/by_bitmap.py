'''

Description:

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''



class Solution:
    
    def subsets(self, nums):

        size = len(nums)

        upper_bound = 1 << size

        solution = [ [ nums[i]for i in range(size) if serial_num & (1<<i) ] for serial_num in range(upper_bound)]

        return solution


# n : the length of input list

## Time Complexity: O( 2^n )
#
# The overhead in time is the cost of subset generation, which is of O( 2^n )

## Space Complexity: O( 2^n )
#
# The overhead in space is the storage for all subsets, which is of O( 2^n ) 


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().subsets( nums = [1,2,3] )
        self.assertCountEqual(result, [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ] )



if __name__ == '__main__':

    unittest.main()