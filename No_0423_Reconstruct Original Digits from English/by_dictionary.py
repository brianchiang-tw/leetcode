'''

Description:

Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"



Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.

'''

from collections import Counter, defaultdict

class Solution:
    def originalDigits(self, s: str) -> str:

        
        # ----------------------------------------------------------
        
        def mapping_rebuild( digit_occ_dict , char_occ_dict ):
            
            
            ## Rebuild the number and its occurrence from character frequency analysis
            
            
            # "z" only shows up in "zero"
            digit_occ_dict [0] = char_occ_dict['z']

            # "w" only shows up in "two"
            digit_occ_dict [2] = char_occ_dict['w']

            # "u" only shows up in "four"
            digit_occ_dict [4] = char_occ_dict['u']

            # "x" only shows up in "six"
            digit_occ_dict [6] = char_occ_dict['x']

            # "g" only shows up in "eight"
            digit_occ_dict [8] = char_occ_dict['g']

            # "o" only shows up in "zero", "one", "two", "four"
            digit_occ_dict [1] = char_occ_dict['o'] - digit_occ_dict [0] - digit_occ_dict [2] - digit_occ_dict [4]

            # "h" only shows up in "three", "eight"
            digit_occ_dict [3] = char_occ_dict['h'] - digit_occ_dict [8]

            # "f" only shows up in "four", "five"
            digit_occ_dict [5] = char_occ_dict['f'] - digit_occ_dict [4]

            # "s" only shows up in "six", "seven"
            digit_occ_dict [7] = char_occ_dict['s'] - digit_occ_dict [6]

            # "i" only shows up in "five", "six", "eight", "nine"
            digit_occ_dict [9] = char_occ_dict['i'] - digit_occ_dict [5] - digit_occ_dict [6] - digit_occ_dict [8]

            return
        # ----------------------------------------------------------
        
        ## dictionary of input s
        # key: ascii character
        # value: occurrence of ascii character
        char_occ_dict = Counter(s)
        
        ## dictionary
        # key: digit
        # value: occurrence of digit
        digit_occ_dict = defaultdict( int )
        
        # rebuild digit-occurrence mapping from input s and its char-occurrence mapping
        mapping_rebuild( digit_occ_dict , char_occ_dict)
        
        # rebuild digit string in ascending order
        digit_string = "".join( (str(digit) * digit_occ_dict [digit]) for digit in range(0, 10) )
        
        return digit_string


# n : the character length of input string s

## Time Complexity : O( n )
#
# The overhead in time is the cost of dictionary building, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage of dictionary, which is of O( 10 ) = O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().originalDigits
        return 

    def test_case_1( self ):

        result = self.solver( s = "owoztneoer" )
        self.assertEqual(result, "012")

    def test_case_2( self ):

        result = self.solver( s = "fviefuro" )
        self.assertEqual(result, "45")        


if __name__ == '__main__':

    unittest.main()        