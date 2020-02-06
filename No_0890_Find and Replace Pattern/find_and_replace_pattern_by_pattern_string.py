'''

Description:

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20

'''



from typing import List
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def helper( s ):
            
            # dictionary
            # key   : character
            # value : serial number in string type
            char_index_dict = dict()
            
            # given each unique character a serial number
            for character in s:
                
                if character not in char_index_dict:
                    char_index_dict[character] = str( len(char_index_dict) )
            
            
            # gererate corresponding pattern string
            return ''.join( map(char_index_dict.get, s) )

        #--------------------------------------------------------    
            
        pattern_string = helper(pattern)
        
        demo = [ helper(word) for word in words ]
        print( demo )

        return [ word for word in words if helper(word) == pattern_string ]
                


# n : the length of input array, words.
# k : the average length of words.

## Time Complexity: O( n * k )
#
# The overhead in time is the cost of list comprehension, which is of O( n ),
# and the for loop, iterating on character, which is of O( k )
#
# It takes O( n * k ) in total.


## Space Complexity: O( n * k )
#
# The overhead in space is the storage for output list comprehension, which is of O( n * k )

        
        
def test_bench():

    test_data = [
                    (["abc","deq","mee","aqq","dkd","ccc"], "abb" )
                ]

    for words, pattern in test_data:

        print( Solution().findAndReplacePattern(words, pattern))
    
    return



if __name__ == '__main__':
    
    test_bench()