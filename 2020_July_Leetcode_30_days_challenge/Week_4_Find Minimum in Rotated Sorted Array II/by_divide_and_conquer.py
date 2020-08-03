'''

Description:

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1


Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?

'''


from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        def helper(left, right):
            
            if right - left <= 1:
                # Base case:
                # only one or two elements remain
                return min(nums[left], nums[right])
            
            
            
            # General case
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[right]:
                # minimum is on the left half
                return helper(left, mid)
            
            elif nums[mid] > nums[right]:
                # minimum is on the right half
                return helper(mid+1, right)
            
            else:
                # don't know where it is, shorten the search range by 1
                return helper(left, right-1)
            
        # ---------------------------------------------
        
        return helper(left=0, right=len(nums)-1)


# n : the length of input list, nums


## Time Complexity: O( n )
#
# The overhead in time is the cost of divide-and-conquer, which is of O( log n ) on average, and O( n ) in worst case.

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( log n ) on average, and O( n ) in worst case.



import unittest

class Testing(unittest.TestCase):


    def unit_test_1(self):
        result = Solution().findMin(nums=[1,3,5])
        self.assertEqual(result, 1)


    def unit_test_2(self):
        result = Solution().findMin(nums=[2,2,2,0,1])
        self.assertEqual(result, 0)



if __name__ == '__main__':

    unittest.main()



