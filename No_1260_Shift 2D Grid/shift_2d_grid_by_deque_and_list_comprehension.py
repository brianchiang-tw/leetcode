'''

Description:

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.



Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]



Example 2:

Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]



Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]




Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100


'''



'''
Hint:
We can reuse the solution(i.e., implementaion) of Leetcode No_189 Rotate Array, as a helper to save time.

Review:
[Leetcode No_189 Rotate Array](https://leetcode.com/problems/rotate-array/).
'''

from collections import deque
from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        # get dimension of grid
        rows, cols = len(grid) , len(grid[0])
        
        total_num_of_elements = cols * rows
        
        # eliminate redundant shifts
        k = k % total_num_of_elements
        
        if k == 0:
            # Quick response: 
            # if k == 0, the same as original
            return grid
        
        else:
            
            # flatten grid to 1D array
            flatten_arr = deque( [ element for row in grid for element in row ] )
            
            # right shift k times
            flatten_arr.rotate(k)
            
            # construct grid of right shift k 
            grid_shift_k = [ [ flatten_arr[y*cols+x] for x in range(cols)] for y in range(rows) ]
            
            return grid_shift_k
        


# m,n : the dimension of row, and columns of input 2D array, grid.

## Time Complexity: O( m * n )
#
# The overhead in time is the list comprehension, which are of O( m * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for output 2D matrix, grid_shift_k, which if of O( m * n )


def test_bench():

    test_data = [
                    ([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4),
                    ([[1,2,3],[4,5,6],[7,8,9]], 8),
                    ([[1,2,3],[4,5,6],[7,8,9]], 9),
                    ([[1,2,3],[4,5,6],[7,8,9]], 10)
                ]

    # expected output:
    '''
    [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
    [[2, 3, 4], [5, 6, 7], [8, 9, 1]]
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    '''


    for matrix, k in test_data:

        print( Solution().shiftGrid(matrix, k) )
    
    return 



if __name__ == '__main__':

    test_bench()