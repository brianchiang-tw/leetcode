'''

Description:

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

'''


class Solution:
    def toLowerCase(self, s: str) -> str:
        
        # for uppercase judgement
        ascii_of_Z, ascii_of_A = ord('Z'), ord('A')
        
        # difference of ascii between uppercase and lowercase of the same letter
        delta = ord('a') - ord('A')
        
        # lambda for lowercase trasform
        tolower = lambda char: chr( ord(char) + delta ) if ascii_of_Z >= ord(char) >= ascii_of_A else char
        
        return ''.join( map(tolower, s) )


# n : the length of input string s

## Time Complexity: O( n )
#
# The overhead in time is the map( tolower, s) operation and ''.join(...), which is if O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output ''.join( ... ), which is of O( n ).



def test_bench():

    test_data = [
                    "Hello",
                    "here",
                    "LOVELY"
                ]

    # expected output:
    '''
    hello
    here
    lovely
    '''

    for s in test_data:

        print( Solution().toLowerCase(s) )

    return



if __name__ == '__main__':

    test_bench()