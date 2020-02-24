'''

Description:

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''



from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # first index is the insertion index on the left
        first = bisect_left( nums, target )
        
        # last index is the insertion index on the right - 1
        last = bisect_right( nums, target )-1
        
        if first > last:
            # target does not exist in nums
            return [-1, -1]
        else:
            # target exist, report indices
            return [ first, last ]



# n : the length of input array, nums.

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The voerhead in space is the storage for result output, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array target')
def test_bench():

    test_data = [
                    TestEntry( array = [5,7,7,8,8,10], target = 8 ),
                    TestEntry( array = [5,7,7,8,8,10], target = 6 ),
                ]

    # expected output:
    '''
    [3, 4]
    [-1, -1]
    '''

    for t in test_data:

        print( Solution().searchRange( nums = t.array, target = t.target) )
    
    return 



if __name__ == '__main__':

    test_bench()