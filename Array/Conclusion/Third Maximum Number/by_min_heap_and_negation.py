'''

Description:

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.



Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.



Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

'''



from heapq import heapify, heappop
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        unique_nums = set(nums)

        if len(unique_nums) < 3:
            return max( nums )

        # use native min-heap to find maximal number
        unique_nums = [ -e for e in unique_nums]
        
        # build min-heap on input nums in-place
        heapify( unique_nums )
        
        # pop 3rd maximum element
        for _ in range(3):
            value = heappop( unique_nums )
            
        return -value



# n : the length of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the cost of set building and heap building, which are of O( n ).

## Space Complexity: O()
#
# The overhead in space is the storage for extra set and list, unique_nums, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [3, 2, 1] ),
                    TestEntry( sequence = [1, 2] ),
                    TestEntry( sequence = [2, 2, 3, 1] ),
                ]

    # expected output:
    '''
    1
    2
    1
    '''

    for t in test_data:

        print( Solution().thirdMax( nums = t.sequence) )
    
    return



if __name__ == '__main__':

    test_bench()