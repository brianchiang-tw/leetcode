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
    def canJump(self, nums: List[int]) -> bool:
        
        furthest_coverage, destination = nums[0], len(nums)-1
        
        # extend furthest coverage from start point
        for cur_index in range( 1,len(nums) ):
            
            if cur_index > furthest_coverage:
                
                # Furthest coverage is too short.
                # We cannot reach current index, thus we cannot get to destination                
                return False
            
            
            elif furthest_coverage >= destination:
                
                # We can reach destination by jump                
                return True
                
            # update furthest coverage on each grid
            furthest_coverage = max( furthest_coverage, cur_index+nums[cur_index] )
            
            
        return furthest_coverage >= destination



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the loop iterating on cur_index, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the loop index, and variable for coverage maintain, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [2,3,1,1,4] ),
                    TestEntry( sequence = [3,2,1,0,4] ),
                    TestEntry( sequence = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5] ),
                    TestEntry( sequence = [2,0] ),
                    TestEntry( sequence = [0] ),
                    TestEntry( sequence = [0,2] ),
                ]

    # expected output:
    '''
    True
    False
    True
    True
    True
    False
    '''

    for t in test_data:

        print( Solution().canJump( t.sequence ) )
    
    return 




if __name__ == '__main__':

    test_bench()        