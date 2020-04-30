'''

Description:

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.



Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.



Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

'''



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # padding one space for empty string representation
        text1 = ' ' + text1
        text2 = ' ' + text2

        w, h = len(text1), len(text2)

        dp_table = [ [ 0 for x in range(w) ] for y in range(h) ]

        # update dynamic programming table with optimal substructure
        for y in range(1, h):
            for x in range(1, w):

                if text1[x] == text2[y]:
                    # with the same character
                    # extend the length of common subsequence
                    dp_table[y][x] = dp_table[y-1][x-1] + 1
                
                else:
                    # with different characters
                    # choose the optimal subsequence
                    dp_table[y][x] = max( dp_table[y-1][x], dp_table[y][x-1] )

        return dp_table[-1][-1]



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'text1 text2')
def test_bench():

    test_data = [
                    TestEntry( text1 = "abcde", text2 = "ace"),
                    TestEntry( text1 = "abc", text2 = "abc"),
                    TestEntry( text1 = "abc", text2 = "def"),
                ]

    # expected output:
    '''
    3
    3
    0
    '''

    for t1, t2 in test_data:

        print( Solution().longestCommonSubsequence( text1= t1, text2=t2) )
    
    return



if __name__ == '__main__':

    test_bench()    