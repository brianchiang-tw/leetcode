'''

Description:

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true



Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.

'''



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    
        iterator_for_t = iter(t)

        return all( char_of_s in iterator_for_t for char_of_s in s )



# n : the character length of input t
# m : the character length of input s

## Time Complexity: O( n )
#
# The ovehead in time is the cost of linear scan, which is of O( n )

## Space Complexity: O( m )
#
# The overhead in space is the storage for boolean flag in generator expression, which is of O( m )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 's t')

def test_bench():

    test_data = [
                    TestEntry( s = "abc", t = "ahbgdc"),
                    TestEntry( s = "axc", t = "ahbgdc"),
                    TestEntry( s = "abcdefghijklmnopq", t = "ahbgdc"),
                    TestEntry( s = "", t = "ahbgdc"),
                    TestEntry( s = "a", t = "ahbgdc"),
                ]

    # expected output:
    '''
    True
    False
    False
    True
    True
    '''

    for t in test_data:

        print( Solution().isSubsequence(*t))
    
    return



if __name__ == '__main__':

    test_bench()