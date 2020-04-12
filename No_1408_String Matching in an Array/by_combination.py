'''

Description:

Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.



Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.

'''



from itertools import combinations
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        substr = set()
        
        for word_1, word_2 in combinations( words, 2):
    
            if ( word_1 in word_2 ):
                substr.add( word_1 )
            
            elif ( word_2 in word_1 ):
                substr.add( word_2 )
        
        return [ *substr ]



# n : the length of input list, words.
# k : the average character length of words

## Time Complexity: O( n^2 * k)
#
# The overhead in time is the cost of combination, C(n, 2), which is of O( n^2 )
# And the substring checking takes O( k ).
#
# It takes O( n^2 * k ) in total.

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'words')
def test_bench():

    test_data = [
                    TestEntry( words = ["mass","as","hero","superhero"] ),
                    TestEntry( words = ["leetcode","et","code"] ),
                    TestEntry( words = ["blue","green","bu"] ),
                ]

    # expected output:
    '''
    ['as', 'hero']
    ['et', 'code']
    []
    '''

    for t in test_data:

        print( Solution().stringMatching( words = t.words ) )

    return



if __name__ == '__main__':

    test_bench()