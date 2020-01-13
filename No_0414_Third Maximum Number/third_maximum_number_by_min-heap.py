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


import heapq
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # use native min-heap to find maximal number
        negation = lambda x: -x
        nums = list( map( negation, nums) )
        
        # build min-heap on input nums in-place
        heapq.heapify( nums )
        
        # record global max for nums' length < 3
        global_max = 0

        # record lastest max element and previous max element
        cur_max_element, prev_max_element = -2**31, -2**31

        # record count of distinct max
        distinct_max = 0
        while nums and distinct_max != 3:
            
            # get currnet max element from min-heap
            cur_max_element = heapq.heappop(nums)
            
            # update global max
            if distinct_max == 0:
                global_max = cur_max_element
            
            # update count of distinct max
            if cur_max_element != prev_max_element:
                distinct_max += 1
                prev_max_element = cur_max_element
        
        
        if distinct_max != 3:
            # nums is too short, without 3rd maximum element
            return negation( global_max )
        else:
            # nums is long enough to have 3rd maximum element
            return negation( cur_max_element )



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
    