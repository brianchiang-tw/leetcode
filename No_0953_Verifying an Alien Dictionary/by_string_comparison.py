'''

Description:

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.



Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.



Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

'''



from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
		# Step 1:
		# Build the index <-> character mapping relation based on givern alien order
		
        ## dictionary
        # key: alien character
        # value: index of alien character
        char_idx_dict = { char: idx for idx, char in enumerate(order) }
        
        size = len(words)
        
		
		# Step 2:
        # Convert words to numerical mapping by dictionary
		
        numerical_mapping = [[char_idx_dict[char] for char in word] for word in words]
        
		
		# Step 3:
        # Check numerical mapping is sorted in ascending order
		
        for i in range(0, size-1):
            
            if numerical_mapping[i] > numerical_mapping[i+1]:
                
                # Reject if we find out-of-order
                return False
        
        # Accept, otherwise.
        return True



# w : total character length of input string list

## Time Complexity: O( w )
#
# The overhead in time is the cost of character comparison, which is of O( w )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for dictionary, which is of O( 26 ) = O( 1 )



import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().isAlienSorted
        return

    def test_case_1( self ):
        
        result = self.solver(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
        self.assertEqual(result, True)

    def test_case_2( self ):
        
        result = self.solver(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz")
        self.assertEqual(result, False)


    def test_case_3( self ):
        
        result = self.solver(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz")
        self.assertEqual(result, False)



if __name__ == '__main__':

    unittest.main()

