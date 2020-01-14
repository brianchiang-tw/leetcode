'''

Description:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

'''



from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        prev_num = -1
        zero_length = 0
        
        for i,x in enumerate(nums):
            
            if x == 0:
                
                if prev_num == 0:
                    # increase zeros length by 1
                    zero_length += 1
                
                else:
                    # reset zeros length
                    zero_length = 1
                    
            else:
                
                if zero_length != 0:
                    # swap non-zero element with zero, and keeping original relative order in array nums
                    nums[ i - zero_length ], nums[i] = nums[i], nums[ i - zero_length ]
                
            # update previous number
            prev_num = nums[i]



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on (i, x), which is of O( n ).

## Space Complexity: O( 1 )
# 
# The overhead in space is the zero length counter as well as swapping buffer, which is of O( 1 ).
 


def test_bench():

    test_data = [
                    [0,1,0,3,12],
                    [0,1,0,1,0],
                    [0,1,0,0,2],
                    [1,0,2,0,3],
                    [1,0,2,0,0,3],
                    [0,0,0,0,1,2],
                    [0,0,0,0,0,2]
                ]

    # expected output:
    '''
    [1, 3, 12, 0, 0]
    [1, 1, 0, 0, 0]
    [1, 2, 0, 0, 0]
    [1, 2, 3, 0, 0]
    [1, 2, 3, 0, 0, 0]
    [1, 2, 0, 0, 0, 0]
    [2, 0, 0, 0, 0, 0]
    '''
    for sequence in test_data:
        
        Solution().moveZeroes(sequence) 
        print( sequence )
    
    return



if __name__ == '__main__':

    test_bench()