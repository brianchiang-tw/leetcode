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



# n : the size of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the heapify() and the while loop iterating on nums, which are of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the record of maximal value, which is of O( 1 ).




def test_bench():

    test_data = [
                    [3, 2, 1],
                    [1, 2],
                    [100],
                    [100,99,99],
                    [100,98,97],
                    [100,99,99,98],
                    [100,99,99,98,97]
                ]

    # expected output:
    '''
    1
    2
    100
    100
    97
    98
    98
    '''


    for sequence in test_data:
        print( Solution().thirdMax(sequence) )

    return 



if __name__ == '__main__':

    test_bench()
    