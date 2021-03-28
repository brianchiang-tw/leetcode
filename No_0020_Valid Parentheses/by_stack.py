'''

Description:

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true



Example 2:

Input: "()[]{}"
Output: true



Example 3:

Input: "(]"
Output: false



Example 4:

Input: "([)]"
Output: false



Example 5:

Input: "{[]}"
Output: true

'''


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
		## dictionary
		# key: right bracket
		# value: corresponding left bracket
        pair = {
                ')':'(',
                ']':'[',
                '}':'{',
                }
        
        for char in s:
            
            if char in pair:
                # check when we meet right parenthesis
                
                if (not stack) or ( stack and (stack[-1] != pair[char]) ):
                
                    # parenthesis mismatch
                    return False
                
                else:
                    
                    # parenthesis match
                    stack.pop()
            
            else:
                # push left parenthesis into stack
                stack.append( char )
        
        
        # Accept if all parenthesis pair are matched.
        return not stack


# n : the length of input string s

## Time Complexity: O( n )
#
# The overhead is the for loop to linear scan each character in s


## Space Complexity: O( n )
#
# The overhead is the variable to keep a stack to record the left braces including '(', '[' and '{'
# The size of stack is at most O( N )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().isValid( s="()" )
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().isValid( s="()[]{}" )
        self.assertEqual(result, True)


    def test_case_3( self ):

        result = Solution().isValid( s="(]" )
        self.assertEqual(result, False)


    def test_case_4( self ):

        result = Solution().isValid( s="([)]" )
        self.assertEqual(result, False)


    def test_case_5( self ):

        result = Solution().isValid( s="{[]}" )
        self.assertEqual(result, True)



# entry point of main
if __name__ == '__main__':

    unittest.main()