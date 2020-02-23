'''

Description:

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.



Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
 


Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
 

Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].

'''



from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Initialization:
        # Left hand side be empty, and
        # Right hand side holds all weights.
        total_weight_on_left, total_weight_on_right = 0, sum(nums)

        for idx, current_weight in enumerate(nums):

            total_weight_on_right -= current_weight

            if total_weight_on_left == total_weight_on_right:
                # balance is met on both sides
                # i.e., sum( nums[ :idx] ) == sum( nums[idx+1: ] )
                return idx

            total_weight_on_left += current_weight

        return -1



# n : the length of input array, nums.

## Time Complexity: O( n )
#
# The overhead in time is the computation of sum(nums), and the for loop, which are of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index, and partial sum, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [1, 7, 3, 6, 5, 6] ),
                    TestEntry( sequence = [1, 2, 3] ),
                    TestEntry( sequence = [3, 2, 5, 4, 1] ),
                ]

    # expected output:
    '''
    3
    -1
    2
    '''

    for t in test_data:

        print( Solution().pivotIndex(t.sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()