'''

Description:

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''

from typing import List
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        xor_result = 0
        for x in nums:
            xor_result ^= x
            
        return xor_result


# N : the length of input list

## Time Complexity : O( N )
#
# Computing exclusive OR (i.e., XOR ) takes O( N ) with scanning each element in input nums.

## Space Complexity : O( 1 )
#
# The overhead in space is the varible for loop element as well as XOR computation with fixed size

def test_bench():

    test_data = [
                    [2, 1, 4, 1 , 2],
                    [1, 1, 2]
                ]


    # expected output:
    '''
    4
    2
    '''

    for series in test_data:

        print( Solution().singleNumber(series) )

    return



if __name__ == '__main__':

    test_bench()