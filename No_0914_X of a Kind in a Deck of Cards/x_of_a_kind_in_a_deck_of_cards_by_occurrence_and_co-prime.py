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



from collections import Counter
from math import gcd
from typing import List
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        if len(deck) < 2:
            return False
        
        card_occ_dict = Counter( deck )
        
        min_occ = min( list( card_occ_dict.values() ) )
        for card, occ in card_occ_dict.items():
            
            # occ and min_occ is co-prime
            if gcd(occ, min_occ) == 1:
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