'''

We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]



Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]



Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]



Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]



Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
 

Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].

'''


from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        # union operation in Counter() means updating with maximum occurrence
        max_occurrence_of = lambda d1, d2: (d1 | d2)
        
        # intersection operation in Counter() means updating with minimum occurrence
        min_occurrence_of = lambda d1, d2: (d1 & d2)
        
        
        ## dictionary
        # key: distinct character
        # value: max occurence of distinct character among words in B
        max_char_occ_dict_of_b = Counter()
        
        
        # compute maximum occrrence of distinct character
        
        for b in B:
            max_char_occ_dict_of_b = max_occurrence_of( max_char_occ_dict_of_b, Counter(b) )
        

        # if Counter(a) can cover max_char_occ_dict_of_b, than a is universal word
        
        universal_words = []
        
		# scan each word in A
        for a in A:
            
            if min_occurrence_of( Counter(a), max_char_occ_dict_of_b ) == max_char_occ_dict_of_b:
                
                universal_words.append( a )
                
        return universal_words


# m : total characters from list A
# n : total characters from list B

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of dictionary operation, which is of O( A + B )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage of dictioanry, which is of O( 26 ) = O( 1 )

import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().wordSubsets
        return

    def test_case_1( self ):

        result = self.solver( A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"] )
        self.assertCountEqual(result, ["facebook","google","leetcode"] )
        return 

    def test_case_2( self ):

        result = self.solver( A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"] )
        self.assertCountEqual(result,  ["apple","google","leetcode"] )
        return 

    def test_case_3( self ):

        result = self.solver( A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"] )
        self.assertCountEqual(result,  ["facebook","google"] )
        return 

    def test_case_4( self ):

        result = self.solver( A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"] )
        self.assertCountEqual(result,  ["google","leetcode"] )
        return 

    def test_case_5( self ):

        result = self.solver( A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"] )
        self.assertCountEqual(result,  ["facebook","leetcode"] )
        return 


if __name__ == '__main__':

    unittest.main()