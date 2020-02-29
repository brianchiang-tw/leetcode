'''

Description:

Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

 

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
Example 4:

Input: digits = [0,0,0,0,0,0]
Output: "0"
 

Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
The returning answer must not contain unnecessary leading zeros.

'''



from collections import defaultdict
from functools import reduce
from typing import List

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        
        digits.sort(reverse = True)
        
        remainder_dict = defaultdict( list)
        summation = 0
        
        for number in digits:
            
            summation += number
            remainder_dict[number % 3].append( number )

            
        if summation == 0:
            # Quick response for all-zero digits case
            return "0"
            
        ## Redundant remainder removal for modulo 3 system            
        redundant = summation % 3     
        if redundant != 0:
            
            if remainder_dict[redundant]:
                remainder_dict[redundant].pop()
            else:
                
                if len(remainder_dict[3-redundant]) >= 2:
                    remainder_dict[3-redundant].pop()
                    remainder_dict[3-redundant].pop()
                else:
                    return ""

        candidates = remainder_dict[0] + remainder_dict[1] + remainder_dict[2]
        
        if not candidates:
            # Quck response if no digits remain after removal of redundant remainder
            return ""
        
        # Keep digits in descending order
        candidates.sort( reverse = True )
        
        # Make the number
        func = lambda x, y: 10*x + y
        value = reduce( func, candidates)
        
        # Convert to string form
        return str(value)



# n :　the length input array, digits.

## Time Complexity: O( n log n)
#
# The overhead in time is the cost of sorting, which is of O( n log n ) in Python by timSort.

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, remainder_dict, which is of O( n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [8,1,9]),
                    TestEntry( sequence = [8,6,7,1,0]),
                    TestEntry( sequence = [1]),
                    TestEntry( sequence = [0,0,0,0,0,0]),
                    TestEntry( sequence = [9,8,6,8,6]),

                ]

    # expected output:
    # Note: the third output is empty string '', which means no solution by definition.
    '''
    981
    8760

    0
    966
    '''

    for t in test_data:

        print( Solution().largestMultipleOfThree( t.sequence) )

    return
        


if __name__ == '__main__':

    test_bench()

