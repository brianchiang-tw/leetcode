'''

Description:

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]



Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.



Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

'''



from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        solution = []
        
        word_pool = set(wordDict)
        
        
        if set(s) > set(''.join(wordDict)):
            
            # Quick response if it is impossible to make s
            return []        
        
        #----------------------------------------
        
        def helper(s, words):
            # find all possible generation of s from word pool in DFS
            
            if s == "":
                # base case also known as stop condition
                # s can be generated from word pool
                solution.append(' '.join(words))
                return
            
            
            for prefix in word_pool:
                # general case
                
                if len(prefix) > len(s):
                    
                    # Skip when prefix is longer than s
                    continue
                
                if s.startswith(prefix):
                    
                    # Keep finding in DFS
                    helper(s[len(prefix):], words[:] + [prefix])
                    
            return
        
        #----------------------------------------
        
        helper(s, words=[])
        
        return solution



# n : the character length of s

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )




import unittest

class Testing(unittest.TestCase):

  def test_case_1(self):

    result = Solution().wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"])

    self.assertCountEqual(result, ["cats and dog","cat sand dog"])


  def test_case_2(self):

    result = Solution().wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"])

    self.assertCountEqual(result, ["pine apple pen apple","pineapple pen apple","pine applepen apple"])


  def test_case_3(self):

    result = Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])

    self.assertCountEqual(result, [])



if __name__ == '__main__':

  unittest.main()