'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

'''



from bisect import bisect_left
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        return bisect_left(nums, target)



# n : the length of input array, nums.

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search tree, which is of O( log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array target')
def test_bench():

    test_data = [
                    TestEntry( array = [1,3,5,6], target = 5),
                    TestEntry( array = [1,3,5,6], target = 2),
                    TestEntry( array = [1,3,5,6], target = 7),
                    TestEntry( array = [1,3,5,6], target = 0),
                ]
    

    # expected output:
    '''
    2
    1
    4
    0    
    '''

    for t in test_data:

        print( Solution().searchInsert( nums = t.array, target = t.target ) )

    return 



if __name__ == '__main__':

    test_bench()