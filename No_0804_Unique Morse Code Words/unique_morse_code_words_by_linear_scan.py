'''

Description:

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

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
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        code_book = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        unique_morse_codes = set()
        
        
        
        for word in words:
            
            morse = ''
            for char in word:
                index = ord(char) - ord('a')

                morse += code_book[ index ]
            
            unique_morse_codes.add( morse )
            
        return len( unique_morse_codes )



# m : the max length of single word
# n : the length of input words

## Time Complexity: O( m * n )
#
# The overhead in time is the nested for loops iterating on word and char, which is of O( m * n ).

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for morse_codes, which is of O( m *n )





def test_bench():

    test_data = [
                    ["gin", "zen", "gig", "msg"],
                    ["hello","world","online","judge"]
                ]

    # expected output:
    '''
    2
    4
    '''


    for test_input in test_data :

        print( Solution().uniqueMorseRepresentations( test_input) )
    
    return



if __name__ == '__main__':

    test_bench()