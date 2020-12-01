'''

Description:

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"



Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"



Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"



Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

'''



class Solution:
    def decodeString(self, s: str) -> str:
        
		# record of tuple ( previous token, repeat times of current token)
        stack = []
        
        cur_token, cur_number =  '', 0
        
        for char in s:
            
            if char == '[':
                # meet start symbol '['
                # save current token and current number into stack
                stack.append( (cur_token, cur_number) )
                
                # clear cur_token for new symbol in [ ]
                cur_token = ''
                
                # clear cur_number for new number in [ ]
                cur_number = 0
                
            elif char == ']':
                # meet ending symbol ']'
                # pop previous token and repeat times of current token from stack
                prev_token, repeat_times = stack.pop()
                
                # update current token with specified repeat times
                cur_token = prev_token + cur_token * repeat_times
                
            elif char.isdigit():
            
                # update current number
                cur_number = cur_number*10 + int(char)
            
            else:
                
                # update current token
                cur_token += char
                
                
        return cur_token



# n : the length of input string


## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for stack, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().decodeString(s = "3[a]2[bc]")
        self.assertEqual(result, 'aaabcbc')


    def test_case_2( self ):

        result = Solution().decodeString(s = "3[a2[c]]")
        self.assertEqual(result, 'accaccacc')


    def test_case_3( self ):

        result = Solution().decodeString(s = "2[abc]3[cd]ef")
        self.assertEqual(result, "abcabccdcdcdef")       


    def test_case_4( self ):

        result = Solution().decodeString(s = "abc3[cd]xyz")
        self.assertEqual(result, "abccdcdcdxyz")      


if __name__ == '__main__':

    unittest.main()        