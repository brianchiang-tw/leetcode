'''

Description:

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.



Example 2:

Input: "aba"
Output: False



Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

''' 



class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        s_fold = s[1:] + s[:-1]
        
        return s in s_fold



# n : the charachter length of input string, s.

## Time Complexity: O( n )
#
# The overhead in time is the cost of string concatenation, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for string, s_fold, which is of O( n ).



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().repeatedSubstringPattern( s="abab" )
        self.assertEqual(result, True)

    
    def test_case_2( self ):

        result = Solution().repeatedSubstringPattern( s="aba" )
        self.assertEqual(result, False)

    
    def test_case_3( self ):

        result = Solution().repeatedSubstringPattern( s="abcabcabcabc" )
        self.assertEqual(result, True)



if __name__ == '__main__':

    unittest.main()