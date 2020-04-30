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
                    
                    nums[ idx ], nums[ idx-zero_len ] = nums[ idx-zero_len ], nums[ idx]
                    
                else:
                    # update previous number
                    prev = number



# n : the langth of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index as well as temporary variable, which is of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array')

def test_bench():

    test_data = [
                    TestEntry(array = [0,1,0,3,12] ),
                    TestEntry(array = [0,1,0,0,2] ),
                    TestEntry(array = [1,0,2,0,3] ),
                    TestEntry(array = [1,0,2,0,0,3] ),
                    TestEntry(array = [0,0,0,0,1,2] ),
                    TestEntry(array = [0,0,0,0,0,2] ),
                ]


    # expected output:

    '''
    [1, 3, 12, 0, 0]
    [1, 2, 0, 0, 0]
    [1, 2, 3, 0, 0]
    [1, 2, 3, 0, 0, 0]
    [1, 2, 0, 0, 0, 0]
    [2, 0, 0, 0, 0, 0]
    '''


    for t in test_data:

        Solution().moveZeroes( nums = t.array)
        print( t.array )



    return




if __name__ == '__main__':

    test_bench()