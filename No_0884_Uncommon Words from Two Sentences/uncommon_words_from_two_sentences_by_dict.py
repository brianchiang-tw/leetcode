'''

Description:

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]



Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

'''



from collections import Counter
from typing import List
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        # a storage for tokens, which are splited by whitespace characters
        tokens = []
        
        # add tokens from string A
        tokens.extend( A.split() )
        
        # add tokens from string B
        tokens.extend( B.split() )
        
        # key   : word
        # value : occurrence
        word_occ_dict= Counter( tokens )
        
        uncommon_words = []
        for word, occ in word_occ_dict.items():
            
            # Uncommon word exists either in A or B.
            # Therefore, its occurrence must be 1
            if occ == 1:
                uncommon_words.append( word )
                
        return uncommon_words



# m : number of tokens in A
# n : number of tokens in B

## Time Complexity: O( m + n )
#
# The overhead in time is the for loop in (word, occ), which is of O( m + n ).



## Space Complexity: O( m + n )
#
# The overhead in space is the storage for dictionay, word_occ_dict, which is of O( m + n ).





def test_bench():

    test_data = [
                    ("this apple is sweet", "this apple is sour"),
                    ("apple apple", "banana"),
                ]

    for str_A, str_B in test_data:

        print( Solution().uncommonFromSentences( A=str_A, B=str_B) )

    return 



if __name__ == '__main__':

    test_bench()