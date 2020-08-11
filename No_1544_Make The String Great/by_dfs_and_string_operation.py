'''

Description:

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

 

Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".



Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""



Example 3:

Input: s = "s"
Output: "s"
 

Constraints:

1 <= s.length <= 100
s contains only lower and upper case English letters.

'''



class Solution:
    def makeGood(self, s: str) -> str:
        
        # initialized to '@' for dummy
        prev = '@'
        
        for idx, char in enumerate(s):
            
            if abs( ord(char)-ord(prev) ) == 32:
                
                # remove bad part and keep making remaining string good
                return self.makeGood(s[:idx-1] + s[idx+1:])
            
            prev = char
        
        # all good
        return s



# n : the character length of string s

## Time Complexity: O( n )
#
# The overhead in time is the iteraion with DFS, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().makeGood( s = "leEeetcode" )
        self.assertEqual( result, "leetcode")


    def test_case_2( self ):

        result = Solution().makeGood( s = "abBAcC" )
        self.assertEqual( result, "")


    def test_case_3( self ):
    
        result = Solution().makeGood( s = "s" )
        self.assertEqual( result, "s")


if __name__ == '__main__':

    unittest.main()