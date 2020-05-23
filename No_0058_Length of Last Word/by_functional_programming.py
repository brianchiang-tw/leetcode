'''

Description:

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''




class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        try:
            last_word = next( reversed( s.split() ) )
            return len( last_word )
        
        except StopIteration:
            return 0



# n : the character length of input string

## Time Complexity: O( n )
#
# The overhead in time is the cost linear scan and token parsing, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for temporary token list in run-time, which is of O( n ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')

def test_bench():

    test_data = [
                    TestEntry( string = "Hello World"),
                    TestEntry( string = "Legth of Last Word"),
                    TestEntry( string = "We love programming"),
                ]

    # expected output:
    '''
    5
    4
    11
    '''

    for t in test_data:

        print( Solution().lengthOfLastWord( s = t.string ) )
    
    return



if __name__ == '__main__':

    test_bench()