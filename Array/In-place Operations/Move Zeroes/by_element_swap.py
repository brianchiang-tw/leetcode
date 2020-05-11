'''

Description:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.



Hint #1  

In-place means we should not be allocating any space for extra array. But we are allowed to modify the existing array. However, as a first step, try coming up with a solution that makes use of additional space. For this problem as well, first apply the idea discussed using an additional array and the in-place solution will pop up eventually.



Hint #2  

A two-pointer approach could be helpful here. The idea would be to have one pointer for iterating the array and another pointer that just works on the non-zero elements of the array.

'''



from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        prev, zero_len = None, 0

        for idx, number in enumerate(nums):

            if number == 0:
                
                if prev == 0:
                    zero_len += 1
                    
                else:
                    # update previous number
                    prev = 0
                    zero_len = 1
            
            else:

                if zero_len:
                    
                    nums[ idx ], nums[ idx-zero_len ] = nums[ idx-zero_len ], nums[ idx ]
                    
                else:
                    # update previous number
                    prev = number



# n : the length of input array, nums.

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhea in space is the cost of loop index and temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [0,1,0,3,12] ),
                    TestEntry( sequence = [1,0,2,0,12] ),
                    TestEntry( sequence = [1,0,2,0,3,0,4] ),
                ]                    

    # expected output:
    '''
    [1, 3, 12, 0, 0]
    [1, 2, 12, 0, 0]
    [1, 2, 3, 4, 0, 0, 0]
    '''

    for t in test_data:

        Solution().moveZeroes( nums = t.sequence ) 
        print( t.sequence )

    return



if __name__ == '__main__':

    test_bench()    