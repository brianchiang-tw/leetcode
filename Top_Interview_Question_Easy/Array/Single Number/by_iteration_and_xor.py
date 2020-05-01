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

class Solution:
    def singleNumber(self, nums: List[int]) -> int:    
        
        x = 0
        
        for number in nums:
            
            x ^= number
            
        return x




# N : the length of input list

## Time Complexity : O( n )
#
# Computing exclusive OR (i.e., XOR ) takes O( n ) with scanning each element in input nums.

## Space Complexity : O( 1 )
#
# The overhead in space is the varible for loop element as well as XOR computation with fixed size

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence =  [2, 1, 4, 1, 2] ),
                    TestEntry( sequence = [1, 1, 2] ),
                ]


    # expected output:
    '''
    4
    2
    '''

    for t in test_data:

        print( Solution().singleNumber( t.sequence ) )

    return



if __name__ == '__main__':

    test_bench()

    