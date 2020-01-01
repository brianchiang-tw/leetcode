'''

Description:

Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"



Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.



Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

'''

class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        # tokenize input s, seperated by whitespace characters (space, tab, newline, return, formfeed)
        # re-arrange token in reverse order
        # generate output string, " "(white space) is added between each token pair
        s_regenerate = " ".join(   [ token for token in ( s.split()[::-1] ) if token]   )
        
        return s_regenerate


# n : the total number of tokens in input string

## Time Complexity: O( n )
#
# First, Tokenization takes O( n ) to scan each word and split
# Secnond, to reverse a token list also takes O( n )
# Finally, to insert whilespace between each token pair takes O( n ) as well.

## Space Complexity: O( n )
#
# The overhead in space is storage for string operation,
# including tokenization, order reverse, as well as string join.


def test_bench():

    test_data = ["the sky is blue", "  hello world!  ", "a good   example"]

    # expected output:
    '''
    blue is sky the
    world! hello
    example good a
    '''



    for s in test_data:

        output_string = Solution().reverseWords( s )

        print( output_string )

    
    return




if __name__ == "__main__":

    test_bench()
    
    