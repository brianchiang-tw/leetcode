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
        
        # Implement Kadane's algorithm

        if nums:
            sum_subarray = nums[0]
        else:
            sum_subarray = 0

        cur_acc_sum = 0
        
        for x in nums:
            
            # does x makes sub-array sum bigger than x itself, 
            # if yes then pick it up
            # if no, just restart from x
            cur_acc_sum = max( cur_acc_sum + x, x)

            # update maximal sub-array sum
            sum_subarray = max( sum_subarray, cur_acc_sum )
            
        
        return sum_subarray



# n : the number of elements in input list

## Time Compleixty: O( n )
#
# The overhead in time is the for loop iterating on x, which is of order O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for current accumulate sum and sum of subarray, 
# which is of fixed size O( 1 ).


def test_bench():

    test_data = [
                    [-2,1,-3,4,-1,2,1,-5,4],
                    [-1],
                    [-1,2,3,-2],
                    []
                ]

    for test_arr in test_data:
        print( Solution().maxSubArray( test_arr ) )

    return



if __name__ == '__main__':

    test_bench()
