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



from typing import List
class Solution:
    

    # Greedy strategy
    # Maintain a variable to keep track of frontier_backtracking
    def canJump(self, nums: List[int]) -> bool:
        
        size = len(nums)
        start_point = 0
        frontier_backtracking = size-1
        
        # backtracking from destination to start point
        for i in reversed( range( 0, size-1 ) ):
            
            # update frontier_backtracking as much as possible
            if i + nums[i] >= frontier_backtracking:
                frontier_backtracking = i

        
        return frontier_backtracking == start_point
                


# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the loop iterating on i, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the loop index, and variable for coverage maintain, which is of O( 1 ).



def test_bench():

    test_data = [
                    [2,3,1,1,4],
                    [3,2,1,0,4],
                    [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
                ]

    # expected output:
    '''
    True
    False
    True    
    '''

    for sequence in test_data:

        print( Solution().canJump(sequence) )
    
    return 




if __name__ == '__main__':

    test_bench()