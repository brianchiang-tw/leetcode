'''

Description:

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''



from typing import List

class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # constant for colors
        RED, WHITE, BLUE = 0, 1, 2
        
        # two pointers for RED as well as BLUE
        idx_red, idx_blue = 0, len(nums)-1
        
        i = 0
        while i <= idx_blue :
            
            if nums[i] == RED:
                
                nums[idx_red], nums[i] = nums[i], nums[idx_red]
                
                # update idx for red
                idx_red += 1
            
            
            elif nums[i] == BLUE:
            
                nums[idx_blue], nums[i] = nums[i], nums[idx_blue]
                
                # update idx for blue
                idx_blue -= 1
                
                # i-1 in order to stay and do one more color check on next iteration
                i -= 1
            
            
            # i move forward
            i += 1                



# n : the length of input, nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and two-pointers, which is of O( 1 ).

def test_bench():

    test_data = [2,0,2,1,1,0]

    Solution().sortColors(test_data)

    # expected output:
    '''
    [0, 0, 1, 1, 2, 2]
    '''

    print( test_data )

    return



if __name__ == '__main__':

    test_bench()