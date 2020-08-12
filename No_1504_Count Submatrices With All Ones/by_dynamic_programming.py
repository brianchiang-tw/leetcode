'''

Description:

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

 

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.



Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.



Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21



Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
 

Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1

'''


from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        h, w = len(mat), len(mat[0])
        
        # dp table:
        # record the maximum length of continuous 1 from left-most column to specified column
        dp_acc_of_1 = [ [ 0 for _ in range(w)] for _ in range(h) ]
        
        for y in range(h):
            for x in range(w):
                
                if x == 0:
                    # left-most column
                    dp_acc_of_1[y][x] = mat[y][x]
                    
                else:
                    # not left-most column
                    if mat[y][x] == 1:
                        dp_acc_of_1[y][x] = dp_acc_of_1[y][x-1] + 1
                        
        
        counter_of_rectangle = 0
        
        for y in range(h):
            for x in range(w):
                
                # update the total number of rectangle, whose bottom right anchor point is [y][x]
                
                minimum_width = dp_acc_of_1[y][x]
                
                for h_idx in range(y, -1, -1):
                    
                    minimum_width = min(minimum_width, dp_acc_of_1[h_idx][x])
                    counter_of_rectangle += minimum_width
                    
                    if minimum_width == 0:
                        # no change to make rectangle
                        break
                        
        return counter_of_rectangle



# m : the dimension of height of input mat
# n : the dimension of width of input mat

## Time Complexity: O( m^2 * n )
#
# The overhead in time is the cost of nested loops, which is of O( m^2 * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( m*n )



import unittest
class Tesing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().numSubmat( mat = [[1,0,1],[1,1,0],[1,1,0]] )
        Solution().numSubmat(result, 13)


    def test_case_2(self):
        result = Solution().numSubmat( mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]] )
        Solution().numSubmat(result, 24)


    def test_case_3(self):
        result = Solution().numSubmat( mat = [[1,1,1,1,1,1]] )
        Solution().numSubmat(result, 21)


    def test_case_4(self):
        result = Solution().numSubmat( mat = [[1,0,1],[0,1,0],[1,0,1]] )
        Solution().numSubmat(result, 5)



if __name__ == '__main__':

    unittest.main(0)        