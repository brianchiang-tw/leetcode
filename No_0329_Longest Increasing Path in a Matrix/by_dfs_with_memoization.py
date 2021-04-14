'''

Description:

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].



Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.



Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

'''



class Solution:
    def longestIncreasingPath(self, matrix):
        
        # -------------------------------------------
        def dfs( cur_position ):
            
            
            ## base case aka stop condition:
            if cur_position in table:
                
                # Quick response if cur_position has been explorered
                return table[cur_position]
            
            ## general cases:
            # visit each possible neighbor to compute longest increasing path
            
            longest_length = 0
            for next_pos in (cur_position + 1, cur_position - 1 , cur_position + 1j, cur_position - 1j ):
                
                if next_pos in grids and grids[next_pos] > grids[cur_position]:
                    
                    longest_length = max(longest_length, dfs(next_pos))
            
            # update memoization table, and 1 is the length of current position
            table[cur_position] = 1 + longest_length
            return table[cur_position]
        
        # -------------------------------------------
        
        # memoization for dfs
        table = {}
        
        ## dictionary
        # key: (X + Yj), 2D coordination in matrix. (j is imaginary part to present y axis in 2D coordination)
        # value: corresponding matrix value to (X, Y)
        grids = { x + y * 1j: value for y, row in enumerate(matrix) for x, value in enumerate(row) }
        
        # start DFS on each possible 2D coordination in grids
        return max( map(dfs, grids) )



# m : the height of input matrix
# n : the width of input matrix

## Time Compleity: O( m * n )
#
# The overhead in time is the cost of DFS, each grid is visited at most ocne, which is of O( m * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the storage of dictionary, which is of O( m * n )


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().longestIncreasingPath
        return

    def test_case_1( self ):

        result = self.solver( matrix = [[9,9,4],[6,6,8],[2,1,1]] )
        self.assertEqual(result, 4)


    def test_case_2( self ):

        result = self.solver( matrix = [[3,4,5],[3,2,6],[2,2,1]] )
        self.assertEqual(result, 4)

        
    def test_case_3( self ):

        result = self.solver( matrix = [[1]] )
        self.assertEqual(result, 1)


if __name__ == '__main__':

    unittest.main()