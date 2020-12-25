'''

Description:

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.

'''



from typing import List
import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        # morse pair
        # key: lowercase letters
        # value: morse code
        morse_pair = zip(string.ascii_lowercase, [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])
        
        # mapping table of morse code
        morse_table = dict( morse_pair )
        
        # set of morse code translation
        morse_code_set = set()
        
        # make corresponding morse code translation for each word
        for word in words:
            
            code = ''.join( morse_table[char] for char in word )
            
            morse_code_set.add( code )
        
        # set length is the number of unique morse code translation
        return len(morse_code_set)
                



## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n ).


## Space Complexity: O( n )
#
# The overhead in space is the stoarage for dictionary and set, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().uniqueMorseRepresentations( words = ["gin", "zen", "gig", "msg"] )
        self.assertEqual(result, 2)

    
if __name__ == '__main__':

    unittest.main()