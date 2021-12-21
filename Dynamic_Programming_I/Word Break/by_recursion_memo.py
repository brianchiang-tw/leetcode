from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        

        
        wordSet = set()
        
        min_word_len = float('inf')
        
        for word in wordDict:
            
            wordSet.add(word)
            
            cur_length = len(word)
            min_word_len = min(min_word_len, cur_length)

            
        if len(set(s)) > len("".join(wordSet)):
            
            # Quick response on letter set
            # If s has extra letters, which are not included in wordSet,
            # Then, it is impossible to make s from wordSet
            return False
                    
            
        
        @lru_cache(maxsize=None)
        def dp( i, j ):

            
            if i > j or (j-i+1) < min_word_len:
                
                ## Base case
                # Reject on empty string, or string smaller than shortest word in wordSet
                return False
            
            elif s[i:j+1] in wordSet:
                ## Base case
                # Accecpt on current substring, which is in wordSet
                return True
            
            
            return any( dp(i, k) and dp(k+1, j)  for k in range(i, j) )
            
            
        # ----------------------------------------------
        
        return dp(0, len(s)-1 )


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