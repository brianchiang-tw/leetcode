'''

Description:


Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.



Example 1:

Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.



Example 2:

Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
 


Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m

'''



class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        
        
        rows, cols = n, m
        
        _2d_array = [ [ 0 for i in range(cols) ] for j in range(rows) ]
        
        for operations in indices:
            
            row_index, col_index = operations
            
            # increment for specified row
            for j in range(cols):
                
                _2d_array[row_index][j] += 1
            
        
            # increment for specified column
            for i in range(rows):
                _2d_array[i][col_index] += 1
        
        
        
        number_of_odds = sum( [ _2d_array[j][i] % 2 for i in range(cols) for j in range(rows) ] )
        
        return number_of_odds