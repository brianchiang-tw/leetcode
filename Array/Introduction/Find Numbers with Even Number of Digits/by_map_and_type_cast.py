'''

Description:

Given an array nums of integers, return how many of them contain an even number of digits.
 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.



Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5

'''


from typing import List
from math import log
from math import floor


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        even_digit_width = lambda number: ( len( str(number) ) % 2 == 0 )
        return sum( map(even_digit_width, nums) , 0 )



# n : the number of input list, nums.

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence' )

def test_bench():

    test_data = [
                    TestEntry( sequence = [12,345,2,6,7896] ),
                    TestEntry( sequence = [555,901,482,1771] ),
                ]

    # expected output:
    '''
    2
    1
    '''

    for t in test_data:

        print( Solution().findNumbers( nums = t.sequence) )

    return



if __name__ == '__main__':

    test_bench()