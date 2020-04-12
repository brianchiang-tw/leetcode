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



from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        
        substr = []
        
        for i, word_1 in enumerate(words):
            
            for j, word_2 in enumerate(words):
                
                # check word_1 is substring of word_2
                if i != j and word_1 in word_2:
                    
                    substr.append( word_1 )
                    
                    # avoid repeated element appending
                    break
                    
        return substr



# n : the length of input list, words.
# k : the average character length of words

## Time Complexity: O( n^2 * k)
#
# The overhead in time is the cost of nested loop, which is of O( n^2 )
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