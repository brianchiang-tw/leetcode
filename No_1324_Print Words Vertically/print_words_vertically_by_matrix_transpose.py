'''

Description:

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

 

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"


 
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"



Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 

Constraints:

1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.

'''



from itertools import zip_longest
from typing import List
class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        # split input string into tokens
        tokens = list( s.split() )
        
        # convert to character array
        char_arr = [ list(t) for t in tokens ]
        
        
        # use matrix transpose technique to get vertical order, with whitespace padding
        
        '''
        Example_#1: 
         [HOW]      [HAY]
         [ARE]  ->  [ORO]
         [YOU]      [WEU]
        
        Example_#2:
         [MEOW]   [MC]
         [CAT] -> [EA]
                  [OT]
                  [W ]
        '''
        
        pair = list(  map(list, zip_longest( *tokens, fillvalue = ' ') )  )
        
        
        # convert from character array to string
        vertical_print_string = [ ''.join(p) for p in pair ]
        
        # elinimate trailing whitespaces
        vertical_print_string = [ s.rstrip() for s in vertical_print_string ]
        
        
        return vertical_print_string


# n : the number of words in string
# m : the maximum length among different words

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of matrix transpose, which is of O( m * n ).

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for vertical print, which is of O( m * n ).



def test_bench():

    test_data = [
                    "HOW ARE YOU",
                    "TO BE OR NOT TO BE",
                    "THAT IS THE QUESTION",
                    "CONTEST IS COMING",
                    "CAT MEOW"
                ]

    # expected output:
    '''
    ['HAY', 'ORO', 'WEU']
    ['TBONTB', 'OEROOE', '   T']
    ['TITQ', 'HSHU', 'A EE', 'T  S', '   T', '   I', '   O', '   N']
    ['CIC', 'OSO', 'N M', 'T I', 'E N', 'S G', 'T']
    ['CM', 'AE', 'TO', ' W']    
    '''


    for test_string in test_data:

        print( Solution().printVertically(test_string) )
    
    return



if __name__ == '__main__':

    test_bench()