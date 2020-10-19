'''

Description:

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]



Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.

'''

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        # set for sequence
        sequence = set()
        
        # set for sequence with repetition
        repeated = set()
        
        for i in range( len(s)-9 ):
            
            # make current sequence for i to i+10
            cur_seq = s[i:i+10]
            
            if cur_seq in sequence:
                # check for repetition
                repeated.add( cur_seq )
            
            # add to sequence set
            sequence.add( cur_seq )
        
        return [ *repeated ]



# n : the character length of s

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Comeplexity: O( n )
#
# The overhead in space is the storage for set, which is of O( n )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findRepeatedDnaSequences( s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" )
        self.assertCountEqual(result, ["AAAAACCCCC","CCCCCAAAAA"])

    
    def test_case_2( self ):

        result = Solution().findRepeatedDnaSequences( s="AAAAAAAAAAAAA" )
        self.assertCountEqual(result, ["AAAAAAAAAA"])



if __name__ == '__main__':

    unittest.main()