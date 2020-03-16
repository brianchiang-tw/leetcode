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
        
        dictionary = { letter : idx for idx, letter in enumerate(order) }
        
        def chk_in_order( word1: str, word2: str):
            
            for i in range( min(len(word1), len(word2) ) ):
                
                # current letter is out-of-order
                if dictionary[ word1[i] ] > dictionary[ word2[i] ]:
                    return False
                
                # current letter is in-order
                elif dictionary[ word1[i] ] < dictionary[ word2[i] ]:
                    return True
                
                # if current letter is the same, then compare next one
            
            # if all the same, then comapre string length
            return ( len(word1) < len(word2) )
        
        # --------------------------------------------------------
        
        for idx in range( len(words)-1 ):
            if not chk_in_order( words[idx], words[idx+1] ):
                return False
        
        return True



# n : the number of words in input list, words
# k : the average character length of words

## Time Complexity: O( n * k )
#
# The overhead in time is the cost of outter loop, iterating on words, which is of O( n ).
# and the cost of function chk_in_order, which is of O( k ).
# It takes O( n * k ) in total.

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for dictionary, which is of O( 26 ) = O( 1 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'words order')
def test_bench():

    test_data = [
                    TestEntry( words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz" ),
                    TestEntry( words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz" ),
                    TestEntry( words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz" ),
                ]

    # expected output:
    '''
    True
    False
    False
    '''

    for t in test_data:

        print( Solution().isAlienSorted( words = t.words, order = t.order) )

    return 



if __name__ == '__main__':

    test_bench()