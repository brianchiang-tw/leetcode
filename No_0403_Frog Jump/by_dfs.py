'''

Description:

A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.



Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.



Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.

'''




from typing import List
class Solution(object):
    def canCross(self, stones):
        
        # total number of valid jump index
        n = len(stones)
        
        # valid jump index
        stone_set = set(stones)
        
        # record of visited status
        visited = set()
        
        # source stone index, destination stone index
        source, destination = stones[0], stones[n-1]
        
        # ----------------------------------------
        
        def frog_jump( cur_idx, cur_step):
            
            # Compute current position
            cur_move = cur_idx + cur_step
            
			
			## Base cases:
            if (cur_step <= 0) or (cur_move not in stone_set) or ( (cur_idx, cur_step) in visited ):
                
                # Reject on backward move
                # Reject on invalid move
                # Reject on repeated path
                return False
            
            elif cur_move == destination:
                
                # Accept on destination arrival
                return True
            
			
			## General cases:
			
            # mark current status as visited
            visited.add( (cur_idx, cur_step) )
            
            # explore all possible next move
            return any( frog_jump(cur_move, cur_step + step_offset) for step_offset in (1, 0, -1) )
        
        # ----------------------------------------
        return frog_jump(cur_idx=source, cur_step=1)



# n : the lenth of input array, stones.

## Time Complexity: O( n )
#
# The overhead in time is the cost of DFS traversal on 1D linked list, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n ).


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().canCross( stones=[0,1,3,5,6,8,12,17] )
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().canCross( stones=[0,1,2,3,4,8,9,11] )
        self.assertEqual(result, False)

    
    def test_case_3( self ):

        result = Solution().canCross( stones=[0,2] )
        self.assertEqual(result, False)


if __name__ == '__main__':

    #test_bench()
    unittest.main()