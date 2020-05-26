'''

Description:

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

'''


from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
        size = len(nums)
        
        if not size:
            # Quick response for empty list
            return 0
        
        max_increasing_len = [ 1 for _ in range(size) ]
        
        for end_idx in range(1, size):
            for scan_idx in range(0, end_idx):
                
                if nums[end_idx] > nums[scan_idx] :
                    # update dp table of number @ end_idx is larger than number @ scan_idx
                    max_increasing_len[ end_idx ] = max( max_increasing_len[ end_idx ], max_increasing_len[ scan_idx ] + 1 )
                    
        return max( max_increasing_len )



# n : the length of input list, nums.

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of nested loop, which is of O( n^2 )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')


def test_bench():

    test_data = [
                    TestEntry( sequence = [10,9,2,5,3,7,101,18] ),
                    TestEntry( sequence = [5,4,7,6,10] ),
                ]

    # expected output:
    '''
    4
    3
    '''

    for t in test_data:
        print( Solution().lengthOfLIS( nums = t.sequence) )
    
    return



if __name__ == '__main__':

    test_bench()