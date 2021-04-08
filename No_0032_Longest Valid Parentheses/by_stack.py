'''

Description:

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".



Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".



Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

'''



class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # stack, used to record index of parenthesis
        # initialized to -1 as dummy head for valid parentheses length computation
        stack = [-1]
        
        max_length = 0
        
		# linear scan each index and character in input string s
        for cur_idx, char in enumerate(s):
            
            if char == '(':
                
                # push when current char is (
                stack.append( cur_idx )
                
            else:
                
                # pop when current char is )
                stack.pop()
                
                if not stack:
                    
                    # stack is empty, push current index into stack
                    stack.append( cur_idx )
                else:
                    # stack is non-empty, update maximal valid parentheses length
                    max_length = max(max_length, cur_idx - stack[-1])
                
        return max_length



# n : the character length of s

## Time Compleity: O( n )
#
# The overhead in time is the iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage of stack, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        
        self.solver = Solution().longestValidParentheses
        return 

    def test_case_1( self ):

        result = self.solver( s = "(()" )
        self.assertEqual(result, 2)

    def test_case_2( self ):

        result = self.solver( s = ")()())" )
        self.assertEqual(result, 4)

    def test_case_3( self ):

        result = self.solver( s = "" )
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()