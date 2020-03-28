'''

Description:

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:

Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]



Input: S = "3z4"
Output: ["3z4", "3Z4"]



Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

'''



from typing import List
from string import ascii_letters

'''

Description:

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:

Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]



Input: S = "3z4"
Output: ["3z4", "3Z4"]



Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

'''



from typing import List
from itertools import product

class Solution:
    def letterCasePermutation(self, S):

        permu = [ [char.lower(), char.upper()] if char.isalpha() else char for char in S ]

        return [''.join(i) for i in product(*permu) ]



# n : the length of input string
# k : the number of alphabet characters in input string

## Time Complexity: O( n * 2^k )
#
# The overhead in time is the cost of permutation generation, which is of O( n * 2^k )

## Space Complexity: O( n * 2^k )
#
# The overhead in space is the storage for all permuation output, which is of O( n * 2^k )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')

def test_bench():

    test_data = [
                    TestEntry( string = "a1b2"),
                    TestEntry( string = "3z4"),
                    TestEntry( string = "12345"),
                ]

    # expected output:
    '''
    ['a1b2', 'A1b2', 'a1B2', 'A1B2']
    ['3z4', '3Z4']
    ['12345']
    '''

    for t in test_data:
        print( Solution().letterCasePermutation( S = t.string) )


    return


# n : the length of input string
# k : the number of alphabet characters in input string

## Time Complexity: O( n * 2^k )
#
# The overhead in time is the cost of permutation generation, which is of O( n * 2^k )

## Space Complexity: O( n * 2^k )
#
# The overhead in space is the storage for all permuation output, which is of O( n * 2^k )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')

def test_bench():

    test_data = [
                    TestEntry( string = "a1b2"),
                    TestEntry( string = "3z4"),
                    TestEntry( string = "12345"),
                ]

    # expected output:
    '''
    ['a1b2', 'A1b2', 'a1B2', 'A1B2']
    ['3z4', '3Z4']
    ['12345']
    '''

    for t in test_data:
        print( Solution().letterCasePermutation( S = t.string) )


    return



if __name__ == '__main__':

    test_bench()