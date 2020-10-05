'''

Description:

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3



Example 2:

Input: [3,4,-1,1]
Output: 2



Example 3:

Input: [7,8,9,11,12]
Output: 1



Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

'''


from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        index, size = 0, len(nums)
        
        while index < size:
            
            cur_num = nums[index]
            
            if (index+1 != cur_num) and (0 < cur_num <= size) and (nums[cur_num-1] != cur_num):
                
                # put cur_num to corrsponding bucket
                nums[index], nums[cur_num-1] = nums[cur_num-1], nums[index]
                
            else:
                # update index
                index += 1
                
        # find first missing positive integer
        for index in range(size):
            
            if nums[index] != (index + 1):
                return index+1
            
        return size+1


# n :　the length of nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().firstMissingPositive( nums=[1,2,0] )
        self.assertEqual(result, 3)


    def test_case_2( self ):

        result = Solution().firstMissingPositive( nums=[3,4,-1,1] )
        self.assertEqual(result, 2)


    def test_case_3( self ):

        result = Solution().firstMissingPositive( nums=[7,8,9,11,12] )
        self.assertEqual(result, 1)


if __name__ == '__main__':

    unittest.main()        