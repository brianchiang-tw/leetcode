'''

Description:

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...



Example 1:

Input: "A"
Output: 1



Example 2:

Input: "AB"
Output: 28



Example 3:

Input: "ZY"
Output: 701
 

Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".

'''



class Solution:
    def titleToNumber(self, s: str) -> int:

        result = 0
        for i, char in enumerate(reversed(s)):
            
            result = result + ( ord(char) - ord('A') + 1 ) * (26**i)
            
        return result


# n : the length of string, s

## Time Complexity: O( n )
#
# The overhead in time is the cost of loop iteration, which is of O( n ).

## Space Comeplexity: O( 1 )
#
# The overhead in space is the storage for temporary vairable and loop index, which is of O( 1 ).

import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().titleToNumber( s='A' )
        self.assertEqual(result, 1)

    
    def test_case_2( self ):

        result = Solution().titleToNumber( s='AB' )
        self.assertEqual(result, 28)


    def test_case_3( self ):

        result = Solution().titleToNumber( s='ZY' )
        self.assertEqual(result, 701)



if __name__ == '__main__':

    unittest.main()