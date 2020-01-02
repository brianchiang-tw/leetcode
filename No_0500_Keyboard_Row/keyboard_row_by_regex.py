'''

Description:

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
 

Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

'''


import re
from typing import List
class Solution:
    
    
    def findWords(self, words):
        return list( filter(re.compile('(?i)^([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words) )



# n : the number of word in input list

## Time Complexity: O( n )
#
# The major overhead in time is the for loop iterating on word, which is of O( n )


## Space Complexity: O( n )
#
# The major overhead in space is the storage for output one_row_words, which is of O( n )


def test_bench():

    test_data = [
                    ["Hello", "Alaska", "Dad", "Peace"]
                ]

    # expected output:
    '''
    ['Alaska', 'Dad']
    '''

    for test_words in test_data:

        print( Solution().findWords(test_words) )

    return 



if __name__ == '__main__':

    test_bench()
    