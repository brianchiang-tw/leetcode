'''

Description:

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4



Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

'''


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            mid = left + (right-left) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid-1
                
            else:
                left = mid+1
                
        return -1


# n : the length of nums:

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binar search, which is of O( log n )

## Space Complexity: O( log n )
#
# The overhead in space is the cost of loop index and temporary variable, which is of O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().search( nums = [-1,0,3,5,9,12], target = 9 )
        self.assertEqual(result, 4)


    def test_case_2( self ):

        result = Solution().search( nums = [-1,0,3,5,9,12], target = 2 )
        self.assertEqual(result, -1)


if __name__ == '__main__':

    unittest.main()        