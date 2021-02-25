'''

Description:

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3



Example 2:

Input: s = "IV"
Output: 4



Example 3:

Input: s = "IX"
Output: 9



Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.



Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

'''



class Solution:
    def romanToInt(self, s: str) -> int:
        
        # key: roman symbol
        # value: decimal value
        mapping_table = {   
                            'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000
                        }
        
        # integer value
        number = 0
        
        # scan each roman symbol
        for idx, char in enumerate(s):
            
            # add corresponding value
            number += mapping_table[char]
            
            if idx and ( mapping_table[char] > mapping_table[ s[idx-1] ] ):
                
                # adjustment for IV, IX, XL, XC, CD, CM
                number -= 2 * mapping_table[ s[idx-1] ]
                
        
        return number



## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Spaec Complexity: O( 1 )
#
# The overhead in space is the storage for dictionary, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().romanToInt( s = "III" )
        self.assertEqual(result, 3)


    def test_case_2( self ):

        result = Solution().romanToInt( s = "IV")
        self.assertEqual(result, 4)


    def test_case_3( self ):

        result = Solution().romanToInt( s = "IX")
        self.assertEqual(result, 9)


    def test_case_4( self ):

        result = Solution().romanToInt( s="LVIII" )
        self.assertEqual(result, 58)


    def test_case_5( self ):

        result = Solution().romanToInt( s="MCMXCIV" )
        self.assertEqual(result, 1994)


if __name__ == '__main__':

    unittest.main()