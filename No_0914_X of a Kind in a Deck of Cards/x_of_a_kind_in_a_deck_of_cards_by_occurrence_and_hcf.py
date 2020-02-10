'''

Description:

In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000

'''



from typing import List
from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        if len(deck) < 2:
            # Quick response: 
            # if deck size < 2 (i.e., lower bound of partition size)
            return False
        
        card_occ_dict = Counter( deck )
        
        if len( card_occ_dict ) == 1:
            # Quick response:
            # if deck consists of only one number
            return True
        
        highest_common_factor = card_occ_dict[ deck[0] ]
        for card, occ in card_occ_dict.items():
               
            # The highest common factor of occurrence must be >= 2 to make a successful partition
            highest_common_factor = gcd(highest_common_factor, occ)

            if highest_common_factor == 1:
                return False
                
        return True



# n : the length of input list, deck.

## Time Complexity: O( n log n)
#
# The overhead in time is the for loop iterating on (crad, occ), which is O( n ),
# and the cost of gcd( occ, min_occ), which is of O( log n ).
# In summary, it takes O( n log n).



## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, card_occ_dict, which is of O( n ).


def test_bench():

    test_data = [
                    [1,2,3,4,4,3,2,1],
                    [1,1,1,2,2,2,3,3],
                    [1],
                    [1,1],
                    [1,1,2,2,2,2],
                    [1,1,1,1,2,2,2,2,2,2],
                    [1,1,1,2,2,2,2,2,3,3,3]
                ]

    # expected output:
    '''
    True
    False
    False
    True
    True
    True
    False    
    '''

    
    for sequence in test_data:

        print( Solution().hasGroupsSizeX(sequence) )

    return 



if __name__ == '__main__':

    test_bench()