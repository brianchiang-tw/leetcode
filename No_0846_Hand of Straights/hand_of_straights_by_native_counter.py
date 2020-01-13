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
            # Quick response on special case with W = 1
            # W = 1 is satisfied by making groups of singly set
            return True
        
        if W > size or size % W !=0:
            # Qucik response on special case with W > size
            # impossible to make partition with W > size
            # impossible to make partition when size is not multiple of W
            return False
        
        
        
        # key   : card number
        # value : occurrence
        num_occ_dict = Counter( hand )
        
        set_of_card_number = set(num_occ_dict.keys())
        
        for cur_card_num in set_of_card_number:
            

            # skip cards which are made in straights before
            if num_occ_dict[cur_card_num] == 0:
                continue
            
            # get the occurrence of current card number
            cur_card_num_occ = num_occ_dict[cur_card_num]
            
            for i in range(0,W):
                
                # continouous number for straight
                cont_num = cur_card_num+i
                
                if cont_num not in num_occ_dict:
                    # lack of card with number = (cur_card_num+i)
                    return False
                
                if num_occ_dict[cont_num] < num_occ_dict[cur_card_num]:
                    # cur_card_num has too many cards, impossible to match straights in final
                    return False
                
                # make cur_card_num_occ pair(s) of straights, card number starts from cur_card_num
                num_occ_dict[cont_num] = num_occ_dict[cont_num] - cur_card_num_occ

                
        return True



# n : the length of input list, hand.
# W : the value of input parameter, W.

## Time Complexity: O( n * W )
#
# The overhead in time is the nested loops.
# The outer for loop iterating on cur_card_num is of O( n ).
# The inner for loop iterating on i is of O( W ).
#
# In total, it takes O( n * W ).


## Space Complexity : O( n )
#
# The overhead in space is the storage for the dictionary, num_occ_dict, 
# as well as the set, set_of_card_number, which are of O( n ).



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