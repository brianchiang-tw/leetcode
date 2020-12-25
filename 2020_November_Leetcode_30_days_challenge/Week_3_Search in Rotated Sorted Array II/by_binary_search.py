'''

Description:

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true



Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false



Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # ------------------------------------------------------
        
        def helper(left, right):

            if left > right:
                return False
            
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return True

            else:

                if nums[mid] < nums[right]:
                    # right half is sorted
                    
                    if nums[mid] < target <= nums[right]:
                        return helper(left=mid+1, right=right)
                    else:
                        return helper(left=left, right=mid-1)
                        
                elif nums[mid] > nums[right]:
                    # left half is sorted
                    
                    if nums[left] <= target < nums[mid]:
                        return helper(left=left, right=mid-1)
                    else:
                        return helper(left=mid+1, right=right)
                    
                else:
                    # repeated at mid and right, discard the rightmost element
                    return helper(left=left, right=right-1)
        # ------------------------------------------------------
                    
        return helper(left=0, right=len(nums)-1)


## Time Complexity: O( n )
#
# The overhead in time is the cost of binary search + linear search, which is of O( n )

## Sapce Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().search( nums = [2,5,6,0,0,1,2], target = 0 )
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().search( nums = [2,5,6,0,0,1,2], target = 3 )
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()        