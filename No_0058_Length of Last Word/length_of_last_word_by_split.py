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
        
        tokens = list( s.split() )
        
        if not tokens:
            return 0
        else:
            return len( list( s.split() ) [-1] )



# n : length of input string s

## Time Complexity: O( n )
#
# The overhead in time is split() over s, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for tokens, also of O( n ).



def test_bench():

    test_data = [
                    "Hello World",
                    " ",
                    "",
                    "test"
                ]

    # expected output:
    '''
    5
    0
    0
    4
    '''


    for test_s in test_data:

        print( Solution().lengthOfLastWord(test_s) )

    return 



if __name__ == '__main__':

    test_bench()