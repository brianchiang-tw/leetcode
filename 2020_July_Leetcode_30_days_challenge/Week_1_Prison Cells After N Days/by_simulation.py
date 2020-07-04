'''

Description:

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9

'''



from typing import List
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        def transition( cells: List[int] ):
            
            next_state = [0 for _ in range(8)]
            
            
            for i in range(1, 7):
                
                if (cells[i - 1] + cells[i + 1]) in (0, 2):
                    # occupied
                    next_state[i] = 1
                    
                else:
                    # vacant
                    next_state[i] = 0
                    
            return next_state
        
        # -----------------------------------------------------
        
        # period of transition is 14 by observation
        N %= 14
        if N == 0:
            N = 14
            
        result = cells
        for i in range(N):
            result = transition( result )
            
        return result



## Time Complexity: O( 1 )
#
# The overhead in time is the cost of transition computation, which is of O( 14 ) = O( 1 )

##　Space Complexity: O( 1 )
#
# The overhead in space is the storage for transition table, which is of O( 8 ) = O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().prisonAfterNDays( cells = [0,1,0,1,1,0,0,1], N = 7 )
        self.assertEqual( result, [0,0,1,1,0,0,0,0] )

    
    def test_case_2( self ):

        result = Solution().prisonAfterNDays( cells = [1,0,0,1,0,0,1,0], N = 1000000000 )
        self.assertEqual( result, [0,0,1,1,1,1,1,0] )



if __name__ == '__main__':

    unittest.main()