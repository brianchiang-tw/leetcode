'''

Description:

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true



Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false



Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false



Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

'''



class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        mapping = {}
        
        words = str.split()
        
        if len(pattern) != len(words):
            # length mis-match
            return False
        
        for char, word in zip(pattern, words):
            
            if char in mapping:
                
                if mapping[char] != word:
                    # mapping change is not allowed
                    return False
                
            elif word not in mapping.values():
                # 1-to-1 mapping
                mapping[char] = word
                
            else:
                # n-to-1 mapping is not allowed
                return False
        
        
        return True


# n : the character length of str

## Time Complexity: O( n )
#
# The overhead in time is the cost of token parsing and for-loop iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n )



import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().wordPattern(pattern = "abba", str = "dog cat cat dog")
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().wordPattern(pattern = "abba", str = "dog cat cat fish")
        self.assertEqual(result, False)


    def test_case_3( self ):

        result = Solution().wordPattern(pattern = "aaaa", str = "dog cat cat dog")
        self.assertEqual(result, False)


    def test_case_4( self ):

        result = Solution().wordPattern(pattern = "abba", str = "dog dog dog dog")
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()    
