'''

Description:


Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

 

Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 3.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.



Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]
 

Constraints:

1 <= s.length <= 104
s[i] and c are lowercase English letters.
It is guaranteed that c occurs at least once in s.

'''


from typing import List

class Solution():

    def shortestToChar(self, S: str, C: str) -> List[int]:

        # record of shortest distance
        shortest_dist = []

        size = len( S )

        if size == 1:

            # Quick response for single character test case
            # Description guarantees that character C must exist in string S
            return [ 0 ]

        
        # Propagate distance from left to right
        for idx, char in enumerate(S):

            if char == C:
                shortest_dist.append( 0 )
            
            else:
                if idx == 0:
                    shortest_dist.append( size )

                else:
                    # propagate distance from C on left hand side
                    shortest_dist.append( shortest_dist[-1]+1 )
            

        # Propagate distance from right to left
        for idx in range(2, size+1):
            
            # propagate distance from C on right hand side
            shortest_dist[-idx] = min( shortest_dist[-idx], shortest_dist[-idx+1] + 1 )


        return shortest_dist


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().shortestToChar( S='loveleetcode', C='e')
        self.assertEqual(result, [3,2,1,0,1,0,0,1,2,2,1,0] )

    
    def test_case_2( self ):

        result = Solution().shortestToChar( S='loveleetcode', C='e')
        self.assertEqual(result, [3,2,1,0,1,0,0,1,2,2,1,0] )


if __name__ == '__main__':

    unittest.main()
