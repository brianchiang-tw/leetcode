'''

Description:

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]



Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Hint #1  
The easiest solution would use additional memory and that is perfectly fine.

Hint #2  
The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use the original array somehow to move the elements around. Now, we can place each element in its original location and shift all the elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.

Hint #3  
One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal might potentially help us out by using an example.

Hint #4  
The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its original position while keeping track of the element originally in that position. Basically, at every step, we place an element in its rightful position and keep track of the element already there or the one being overwritten in an additional variable. We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.

'''

from typing import List

class Solution:
    
    
    def reverse(self, nums: List[int], start, end):
        
		# reverse array elements within [start, end] interval
        while start < end:
            
            nums[start], nums[end] = nums[end], nums[start]
            
            start += 1
            end -= 1
            
            
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        
        
        if k > size:
            # eliminate redundant rotation which is over size
            k = k % size 
        
        
            # reverse all elements
        self.reverse( nums, 0, size-1)
        
            # reverse first k elements
        self.reverse( nums, 0, k-1)
        
            # reverse last (size - k) elements 
        self.reverse( nums, k, size-1)
        
        return



# n : the length of nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of reverse, which is of O( n )

## Space Complexity: O( 1 )
# 
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        nums = [1,2,3,4,5,6,7]
        Solution().rotate( nums=nums, k=3)
        self.assertEqual(nums, [5,6,7,1,2,3,4])


    def test_case_2( self ):
        nums = [-1,-100,3,99]
        Solution().rotate( nums=nums, k=2)
        self.assertEqual(nums, [3,99,-1,-100]) 


if __name__ == '__main__':

    unittest.main()               