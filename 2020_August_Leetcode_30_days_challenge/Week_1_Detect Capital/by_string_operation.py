'''

Description:

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

'''



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word == word.upper() or word == word.lower() or word == word.capitalize():
            return True
        
        else:
            return False



# n : the character length of input word

## Time Complexity: O( n )
#
# The overhead in time is the cost of string checking one by one, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 ).

import unittest
class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().detectCapitalUse("USA")
        self.assertEqual(result, True)

    
    def test_case_2(self):

        result = Solution().detectCapitalUse("Usa")
        self.assertEqual(result, True)

    
    def test_case_3(self):

        result = Solution().detectCapitalUse("usa")
        self.assertEqual(result, True)

    
    def test_case_4(self):

        result = Solution().detectCapitalUse("usA")
        self.assertEqual(result, False)


    def test_case_5(self):

        result = Solution().detectCapitalUse("FlaG")
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()

