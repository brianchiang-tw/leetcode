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
        
        words = s.split()
        
        if not s or not words:
            # Quick response for empty string or string full of whitespaces
            return 0
        
        return len( words[-1] )



# n : the character length of input s.

## Time Complexity: O( n )
#
# The overhead in time is the cost of token parsing, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for tokens, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().lengthOfLastWord( s="Hello World" )
        self.assertEqual(result, 5)


    def test_case_2( self ):
    
        result = Solution().lengthOfLastWord( s=" " )
        self.assertEqual(result, 0)



if __name__ == '__main__':

    unittest.main()
    
    