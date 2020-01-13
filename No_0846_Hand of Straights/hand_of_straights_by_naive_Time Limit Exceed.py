'''

Description:

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length

'''



from collections import Counter
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        size = len( hand )
        if W == 1:
            # Quick response on special case on W = 1
            # W = 1 is groups of singly set
            return True
        
        if W > size or size % W !=0:
            # Qucik response on special case on W > size
            # impossible to make partition with W > size
            # impossible to make partition with size is not multiple of W
            return False
        
        
        group_count = 0
        
        num_occ_dict = Counter( hand )
        min_card = min( list(num_occ_dict.keys() ) ) 
        
        
        while num_occ_dict:
            
            if all( [ (min_card+i in num_occ_dict) for i in range (1, W) ] ):
                
                group_count += 1
                
                for i in range(0,W):
                    
                    num_occ_dict[min_card+i] -= 1
                    
                    if num_occ_dict[min_card+i] == 0:
                        
                        del num_occ_dict[min_card+i]
                
                
                if num_occ_dict:
                    # update min_card
                    min_card = min( list(num_occ_dict.keys() ) ) 
                    
            else:
                #print("min_card", min_card)
                return False
            
        
        return True
                
            

def test_bench():

    test_data = [
                    ([1,2,3,6,2,3,4,7,8], 3),
                    ([1,2,3,4,5], 4)
                ]

    # expected output:
    '''
    True
    False
    '''


    for poker_cards, W in test_data:

        print( Solution().isNStraightHand(poker_cards, W) )
    
    return



if __name__ == '__main__':

    test_bench()