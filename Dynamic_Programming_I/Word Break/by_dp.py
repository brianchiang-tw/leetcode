from typing import List
from collections import defaultdict

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_pool = set(wordDict)

        prefix_match = defaultdict(bool)

        # Base case, empty string must be breakable
        prefix_match[0] = True

        size = len(s) 

        for window_end in range( size ):

            for window_start in range(window_end+1):

                postfix = s[window_start:window_end+1]

                if prefix_match[ window_start ] and postfix in word_pool:
                    prefix_match[window_end+1] = True

        return prefix_match[size]


import unittest

class Testing( unittest.TestCase):

    def test_case_1( self ):

        result = Solution().wordBreak( s = "leetcode", wordDict = ["leet","code"] )
        self.assertEqual(result, True)
        return


    def test_case_2( self ):

        result = Solution().wordBreak( s = "applepenapple", wordDict = ["apple","pen"] )
        self.assertEqual(result, True)
        return        



    def test_case_3( self ):

        result = Solution().wordBreak( s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] )
        self.assertEqual(result, False)
        return                


if __name__ == '__main__':

    unittest.main()        