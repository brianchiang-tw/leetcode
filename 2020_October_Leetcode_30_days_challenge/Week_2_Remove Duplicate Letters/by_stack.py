'''

Description:

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"



Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

Hint #1  
Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

'''


from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # dictionary
        # key: char
        # value: occurrence of character
        char_occ_dict = Counter(s)
        

        
        visited = set()
        
        # "0" as global dummy char for comparison, "0" is smaller than all alphabet letters
        result = ["0"]
        
        # scan for each character
        for char in s:
            
            # decrease ocurrence
            char_occ_dict[char] -= 1
            
            # skip this round if current char has been visited and generated
            if char in visited: continue
            
            last_char = result[-1]
            
            # keep lexical order as small as possible by stack
            while (char < last_char) and char_occ_dict.get(last_char, None) > 0:
                
                result.pop()
                visited.discard( last_char )
                last_char = result[-1]
            
            # add current character into stack
            result.append( char )
            visited.add( char )

        # ouptut string, excluding dummy character "0"
        return ''.join(result[1:])


# n : the character length of s

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop with stack, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for stack, which is of O( n )
         


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().removeDuplicateLetters(s="bcabc")
        self.assertEqual(result, "abc")

    
    def test_case_2( self ):

        result = Solution().removeDuplicateLetters( s="cbacdcbc")
        self.assertEqual(result, "acdb")



if __name__ == '__main__':

    unittest.main()
