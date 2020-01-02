'''

Description:

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''

from typing import List
class Solution:
    
    def helper(self, nums, i, j, target):
        
        if j-i < 0:
            return [-1, -1]
        
        if j-i == 0:
            
            if target == nums[i]:
                return [i, i]
            else:
                return [-1, -1]
        
        #if target not in nums[i:j+1]:
        #    return [-1, -1]
        
        mid = ( i + j ) // 2
        mid_value = nums[mid]
        mid_occ = None
        
        if mid_value == target:
            mid_pos = mid
            
            left_first, left_last, right_first, right_last = None, None, None, None
            
            left_occ = ( mid-1 >= i and target == nums[mid-1] )
            right_occ = ( mid+1 <= j and target == nums[mid+1] )
            
            if left_occ and right_occ:
                left_first, left_last = self.helper( nums, i, mid-1, target)
                right_first, right_last = self.helper( nums, mid+1, j, target)
                return left_first, right_last
            
            elif left_occ:
                left_first, left_last = self.helper( nums, i, mid-1, target)
                return left_first, mid_pos
            
            elif right_occ:
                right_first, right_last = self.helper( nums, mid+1, j, target)
                return mid_pos, right_last
            
            else:
                return mid_pos, mid_pos
            
            
            
        elif mid_value > target:
            first, last = self.helper( nums, i, mid-1, target)
            return first, last
        
        else:
            first, last = self.helper( nums, mid+1, j, target)
            return first, last
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        return self.helper( nums, 0, len(nums)-1, target)


'''

test_data:

[5,7,7,8,8,10]
8
[5,7,7,8,8,10]
6
[3,3,3]
3
[1,3]
1
[2,2]
2

'''