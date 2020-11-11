'''

Description:

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.



Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.



Example 3:

Input: s = "triplepillooooow"
Output: 5



Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11



Example 5:

Input: s = "tourist"
Output: 1
 

Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.



Hint #1  
Keep an array power where power[i] is the maximum power of the i-th character.

Hint #2  
The answer is max(power[i]).

'''



class Solution:
    def maxPower(self, s: str) -> int:
        
        # the minimum value for consecutive is 1
        local_max, global_max = 1, 1
        
        # dummy char for initialization
        prev = '#'
        for char in s:
            
            if char == prev:
                
                # keeps consecutive, update local max
                local_max += 1
                
                # update global max length with latest one
                global_max = max( global_max, local_max )
                
            else:
                
                # lastest consective chars stops, reset local max
                local_max = 1
            
                # update previous char as current char for next iteration
                prev = char
        
        
        return global_max


# n : the character length of input string s

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxPower( s="leetcode" )
        self.assertEqual(result, 2)

    
    def test_case_2( self ):

        result = Solution().maxPower( s="abbcccddddeeeeedcba")
        self.assertEqual(result, 5)

    
    def test_case_3( self ):

        result = Solution().maxPower( s="triplepillooooow")
        self.assertEqual(result, 5)


    def test_case_4( self ):

        result = Solution().maxPower( s="hooraaaaaaaaaaay")
        self.assertEqual(result, 11)        


    def test_case_5( self ):

        result = Solution().maxPower( s="tourist")
        self.assertEqual(result, 1)      


if __name__ == '__main__':

    unittest.main()              