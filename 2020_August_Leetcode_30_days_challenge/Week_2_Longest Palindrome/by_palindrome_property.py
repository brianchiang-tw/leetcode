'''

Description:

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.



Example 2:

Input: s = "a"
Output: 1



Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consits of lower-case and/or upper-case English letters only.

'''



from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        total_length = len(s)
        odd_counts = sum(1 for char, occurrence in Counter(s).items() if (occurrence & 1) )
        
        # First, we can choose one character from odds as center of palindrome
        # For example, 'bbabb' or 'bab'.
        
        # If all characters are of even occurrence, then put them on left-hand side and right-hand side evenly.
        # For example, 'bbbffbbb'
        
        # Second, for each characters with odd occurrence, discard one character of its own to make it with even occurrence (therefore they can be palindrome always)
        # For example, 'aaa' -> 'aa', 'ccccc' -> 'cccc'
        
        return (odd_counts > 0) + total_length - odd_counts



# n : the character length of input string, s

## Time Complexity: O( n )
#
# The overhead in time is the cost of generator expression, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for temporary varaible as well as loop index, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().longestPalindrome( s="abccccdd" )
        self.assertEqual(result, 7)


    def test_case_2( self ):

        result = Solution().longestPalindrome( s="a" )
        self.assertEqual(result, 1)


    def test_case_3( self ):

        result = Solution().longestPalindrome( s="bb" )
        self.assertEqual(result, 2)

        

if __name__ == '__main__':

    unittest.main()