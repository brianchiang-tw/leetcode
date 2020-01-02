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
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # dictionary: num_occ
        # key: number
        # value: occurrence of number
        num_occ = Counter(nums)
        
        # find the key with occurrence = 1
        single_number = list(num_occ.keys())[ list(num_occ.values()).index(1) ]
        
        return single_number


# N : the length of input list

## Time Complexity : O( N )
#
# It seems to be O( 1 ) at first glimpse, but actually it takes O( N ).
#
# First creating dictionary takes O( N ) with scanning each element in input nums.
# Second, generating keys and look-up takes O( N ) also.

## Space Complexity : O( N )
#
# The overhead in space is the dictionay, it takes O( N ) to build.

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

    