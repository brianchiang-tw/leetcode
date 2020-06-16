'''

Description:

Given a sentence that consists of some words separated by a single space, and a searchWord.

You have to check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string S is any leading contiguous substring of S.

 

Example 1:

Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.



Example 2:

Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2
Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.



Example 3:

Input: sentence = "i am tired", searchWord = "you"
Output: -1
Explanation: "you" is not a prefix of any word in the sentence.



Example 4:

Input: sentence = "i use triple pillow", searchWord = "pill"
Output: 4



Example 5:

Input: sentence = "hello from the other side", searchWord = "they"
Output: -1
 

Constraints:

1 <= sentence.length <= 100
1 <= searchWord.length <= 10
sentence consists of lowercase English letters and spaces.
searchWord consists of lowercase English letters.

'''



class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        # parse and save each word from sentence
        words = [ *sentence.split() ]
        
        for idx, word in enumerate(words, 1):
            
            if word.startswith(searchWord):
                
                # Accept if searchWord is prefix of current word
                return idx
        
        # Reject if no solution
        return -1



# m : the number of words in sentence
# n : the character length of searchWord

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of loop with prefex checking str.startswith( ... ), which is of O( m * n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )



import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().isPrefixOfWord( sentence = "i love eating burger", searchWord = "burg" )
        self.assertEqual( result, 4 )


    def test_case_2(self):
    
        result = Solution().isPrefixOfWord( sentence = "this problem is an easy problem", searchWord = "pro" )
        self.assertEqual( result, 2 )


    def test_case_3(self):
        
        result = Solution().isPrefixOfWord( sentence = "i am tired", searchWord = "you" )
        self.assertEqual( result, -1 )


    def test_case_4(self):
        
        result = Solution().isPrefixOfWord( sentence = "i use triple pillow", searchWord = "pill" )
        self.assertEqual( result, 4 )

    
    def test_case_5(self):

        result = Solution().isPrefixOfWord( "hello from the other side", searchWord = "they" )
        self.assertEqual( result, -1 )




if __name__ == '__main__':

    unittest.main()