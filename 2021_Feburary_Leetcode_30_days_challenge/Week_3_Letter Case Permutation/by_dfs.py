'''

Description:

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]



Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]



Example 3:

Input: S = "12345"
Output: ["12345"]



Example 4:

Input: S = "0"
Output: ["0"]
 

Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

'''


from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        result = []
        
        # -------------------------------------------------
        def dfs(substr='', idx=0):
            
            if len(substr) == len(S):
                # base case
                result.append( substr)
                
            else:
                # general case
                if S[idx].isalpha():
                    # current char is alphabet, change upper/lower case and go to next level
                    dfs( substr + S[idx].swapcase(), idx+1 )
                
                # go to next level
                dfs( substr + S[idx], idx+1)
            
            return
        
        # -------------------------------------------------
        
        # start permutation generation from empty string, and index = 0
        dfs(substr='', idx=0)
        return result
            