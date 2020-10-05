'''

Description:

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".



Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.



Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''


from collections import defaultdict
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_pool = set(wordDict)
        
        prefix_match = defaultdict(bool)

        # initialization
        prefix_match[0] = True
        
        # iterate each end index of sliding window
        for window_end in range( len(s)+1 ):
            
            # iterate each start index of sliding window
            for window_start in range(window_end+1):
                
                # get current postfix
                postfix = s[window_start:window_end+1]
                
                if prefix_match[window_start] and postfix in word_pool:
                    
                    # update prefix match if both prefix and postfix are matched
                    prefix_match[window_end+1] = True
        
        
        return prefix_match[len(s)]


# n : the lengh of input s

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of string copy in nested-loop, which is of O( n^2 )

## Space Complexity: O( n )
#
# The overhead in space is the storage for string copu and dictionary, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().wordBreak( s="leetcode", wordDict=["leet", "code"] )
        self.assertEqual(result, True)

    
    def test_case_2( self ):

        result = Solution().wordBreak( s="applepenapple", wordDict=["apple", "pen"])
        self.assertEqual(result, True)


    def test_case_3( self ):

        result = Solution().wordBreak( s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"] )
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()        