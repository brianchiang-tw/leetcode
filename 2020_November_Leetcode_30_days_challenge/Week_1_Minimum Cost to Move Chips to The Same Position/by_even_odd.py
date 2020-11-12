'''

Description:

We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

 

Example 1:


Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.



Example 2:


Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.



Example 3:

Input: position = [1,1000000000]
Output: 1
 

Constraints:

1 <= position.length <= 100
1 <= position[i] <= 10^9

'''


from typing import List

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:

        # Two variables for 
        # cost of odd position to even position, and
        # cost of even position to odd position
        odd_to_even, even_to_odd = 0, 0
        
        for position in chips:
            
            # update moving cost
            if position % 2 == 0:
                even_to_odd += 1
            
            else:
                odd_to_even += 1
                
        return min( even_to_odd, odd_to_even )


# n : the length of input array chips

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( 1 )

## Space Compelxity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TsetCase ):

    def test_case_1( self ):

        result = Solution().minCostToMoveChips( position=[1,2,3] )
        self.assertEqual(result, 1)

    
    def test_case_2( self ):

        result = Solution().minCostToMoveChips( position=[2,2,2,3,3] )
        self.assertEqual(result, 2)


    def test_case_3( self ):

        result = Solution().minCostToMoveChips( position=[1,1000000000] )        
        self.assertEqual(result, 1)


if __name__ == '__main__':

    unittest.main()        