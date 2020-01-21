'''

Description:

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

'''



from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        # destination is last index
        destination = size - 1
        
        # record of current coverage, record of last jump index
        cur_coverage, last_jump_index = 0, 0
        
        # counter for jump
        times_of_jump = 0
        
         # Quick response if start index == destination index == 0
        if size == 1:
            return 0
        
        
        # Greedy strategy: extend coverage as long as possible with lazy jump
        for i in range( 0, size):
            
            # extend current coverage as further as possible
            cur_coverage = max( cur_coverage, i + nums[i] )
            

            # forced to jump (by lazy jump) to extend coverage  
            if i == last_jump_index:
            
                # update last jump index
                last_jump_index = cur_coverage
                
                # update counter of jump by +1
                times_of_jump += 1
                
                # check if reached destination already
                if cur_coverage >= destination:
                        return times_of_jump
                
        return times_of_jump



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and variable for coverage and jumps, which is of O( 1 )





def test_bench():

    test_data = [ 
                    [2,3,1,1,4],
                    [1,2,3,2,1,1,2,1]
                ]

    # expected output:
    '''
    2
    5
    '''

    for sequence in test_data:

        print( Solution().jump(sequence) )

    return 



if __name__ == '__main__':

    test_bench()