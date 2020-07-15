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
		
        s_regenerate = " ".join(   ( token for token in reversed( s.split() ) )   )
        
        return s_regenerate



# n : the character length of input string s.

## Time Complexity: O( n )
#
# The overhead in time is the cost of token parsing and string concatenation, which are of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for output variable, s_regenerate, which is of O( n )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().reverseWords(s="the sky is blue")
        self.assertEqual(result, "blue is sky the")        


    def test_case_2(self):

        result = Solution().reverseWords(s="  hello world!  ")
        self.assertEqual(result, "world! hello")        


    def test_case_3(self):

        result = Solution().reverseWords(s="a good   example")
        self.assertEqual(result, "example good a")        



if __name__ == '__main__':

    unittest.main()        