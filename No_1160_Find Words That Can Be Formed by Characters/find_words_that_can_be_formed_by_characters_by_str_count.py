'''

Description:

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.

'''



from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
          
        list_of_success = []
        
        # visit each word
        for word in words:
            
            # check each character
            for character in word:
                
                if word.count( character ) > chars.count( character ):
                    # miss:
                    # chars has no enough characters to make the word
                    break
                    
            else:
                # hit:
                # add the word into list of success
                list_of_success.append( word )
                
                
        return len ( ''.join( list_of_success) )



# m : the length of input list, words.
# n : the maximal length of word in words

## Time Complexity : O( m * n )
#
# The overhead in time is the nested for loops iterating on (word, character), which is of O( m * n )

## Space Complexity : O( m * n )
#
# The overhead in space is the storage for list_of_success, which is of O( m * n )



def test_bench():

    test_data = [
                    (["cat","bt","hat","tree"], "atach"),
                    (["hello","world","leetcode"], "welldonehoneyr")
                ]

    # expected output:
    '''
    6
    10
    '''

    for words, chars in test_data:

        print( Solution().countCharacters(words, chars) )

    return 



if __name__ == '__main__':

    test_bench()