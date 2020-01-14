'''

Description:

There are some chips, and the i-th chip is at position chips[i].

You can perform any of the two following types of moves any number of times (possibly zero) on any chip:

Move the i-th chip by 2 units to the left or to the right with a cost of 0.
Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
There can be two or more chips at the same position initially.

Return the minimum cost needed to move all the chips to the same position (any position).

 

Example 1:

Input: chips = [1,2,3]
Output: 1
Explanation: Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.
Example 2:

Input: chips = [2,2,2,3,3]
Output: 2
Explanation: Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.
 

Constraints:

1 <= chips.length <= 100
1 <= chips[i] <= 10^9

'''



'''
Example explanation:

Input: chips = [2,2,2,3,3]

Position_#2: chip_#1, chip_#2, chip_#3

Position_#3: chip_#4, chip#5

cost_of_even_to_odd = 3 (move chip_#1, chip_#2, chip_#3 from Position_#2 to Position_#3)

cost_of_odd_to_even = 2 (move chip_#4, chip_#5 from Position_#3 to Position_#2)

'''



from typing import List
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        
        cost_odd_to_even = 0
        cost_even_to_odd = 0
        
        size = len(chips)
        
        func = lambda x: x % 2 == 0
        
        cost_even_to_odd = len( list( filter(func, chips) ) )
        cost_odd_to_even = size - cost_even_to_odd
        
        return min( cost_even_to_odd, cost_odd_to_even )



# n : the length of input list, chips.

## Time Complexity: O( n )
#
# The overhead in time is the list(...) and filter(...) over chips, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the math computation varible, which is of O( 1 )


def test_bench():

    test_data = [
                    [1,2,3],
                    [2,2,2,3,3]
                ]

    # expected output:
    '''
    1
    2
    '''

    for chips in test_data:

        print( Solution().minCostToMoveChips(chips))

    return 

if __name__ == '__main__':

    test_bench()