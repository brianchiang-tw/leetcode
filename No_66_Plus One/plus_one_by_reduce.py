'''

Description:

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''

from typing import List
from functools import reduce

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        func = lambda x,y: (10*x + y)
        
        origin = reduce( func, digits )
        
        return list( str(origin+1) )



# n : the number of elements in input digits

## Time Complexity: O( n )
#
# The overhead in time is the join(), map(), str(), as well as list(), all of O( n ).

## Soace Complexity: O( n )
#
# The overhead in space is the storage for output digit list, which is of O( n ).

def test_bench():

    test_data = [
                    [1,2,3,4],
                    [9,9],
                    [9],
                    [0]
                ]


    # expected output:
    '''
    ['1', '2', '3', '5']
    ['1', '0', '0']
    ['1', '0']
    ['1']
    '''


    for seq in test_data:
        print( Solution().plusOne( seq ) )

    return 



if __name__ == '__main__':

    test_bench()