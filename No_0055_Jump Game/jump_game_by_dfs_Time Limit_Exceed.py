'''

Description:

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.



Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

'''



class Solution:
    
    def jumper(self, nums: List[int], index):
        
        size = len(nums)
        
        # base case:
        # stop condition when reaching destination
        if index == size-1:
            return True
        
        max_length_of_jump = nums[index]
        
        # check available jump length
        if max_length_of_jump == 0:
            # no other jump path to go
            return False
        
        flag_of_destination = False
        
        # for every possible jumps
        for i in range(max_length_of_jump+1, 0, -1):
            
            next_jump = index+i
            
            # if next_jump is valid index, then jump to next location
            if next_jump < size:
                flag_of_destination |= self.jumper( nums, next_jump)
        
        return flag_of_destination
    
    def canJump(self, nums: List[int]) -> bool:
        
        return self.jumper( nums, 0 )