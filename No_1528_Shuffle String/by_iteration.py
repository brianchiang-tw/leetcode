'''

Description:

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 

Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.


Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.



Example 3:

Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"



Example 4:

Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
Output: "arigatou"



Example 5:

Input: s = "art", indices = [1,0,2]
Output: "rat"
 

Constraints:

s.length == indices.length == n
1 <= n <= 100
s contains only lower-case English letters.
0 <= indices[i] < n
All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).


'''


from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        size = len(s)
        shuffle_s = [' ' for _ in range(size)]
        
        for idx, char in enumerate(s):
            shuffle_s[ indices[idx] ] = char
            
        return ''.join(shuffle_s)



# n : the character length of string s

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )


## Space Complexity: O( n )
#
# The overhead in space is the storage for output, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().restoreString( s = "codeleet", indices = [4,5,6,7,0,2,1,3] )
        self.assertEqual( result, "leetcode")


    def test_case_2( self ):
    
        result = Solution().restoreString( s = "abc", indices = [0,1,2] )
        self.assertEqual( result, "abc")


    def test_case_3( self ):
        
        result = Solution().restoreString( s = "aiohn", indices = [3,1,4,2,0] )
        self.assertEqual( result, "nihao")


    def test_case_4( self ):
        
        result = Solution().restoreString( s = "aaiougrt", indices = [4,0,2,6,7,3,1,5] )
        self.assertEqual( result, "arigatou")


    def test_case_5( self ):
        
        result = Solution().restoreString( s = "art", indices = [1,0,2] )
        self.assertEqual( result, "rat")



if __name__ == '__main__':

    unittest.main()
