'''

Description:

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # setting for initial value
        if nums:
            max_subarray_sum = nums[0]
        else:
            max_subarray_sum = -2**31

        cur_partial_sum = 0

        # update maximum partial sum by Kadane algorithm
        for number in nums:
            
            # Dies number makes current partial sum bigger?
            # If yes, then pick up current number
            # If no, then restart from current number
            cur_partial_sum = max( cur_partial_sum + number, number )

            max_subarray_sum = max( max_subarray_sum, cur_partial_sum)

        return max_subarray_sum



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array')
def test_bench():

    test_data = [
                    TestEntry( array = [-2,1,-3,4,-1,2,1,-5,4] ),
                    TestEntry( array = [-1] ),
                    TestEntry( array = [-1,2,3,-2] ),
                    TestEntry( array = [] ),
                ]

    # expected output:
    '''
    6
    -1
    5
    -2147483648
    '''

    for t in test_data:
        print( Solution().maxSubArray( nums = t.array) )

    
    return


if __name__ == '__main__':

    test_bench()        