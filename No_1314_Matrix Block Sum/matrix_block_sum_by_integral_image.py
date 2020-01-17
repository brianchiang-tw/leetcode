'''

Description:

Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100

'''


from typing import List
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
            
        h, w = len(mat), len( mat[0])
        integral_image = [ [ 0 for y in range(w) ] for x in range(h) ]
        

        # building integral image to speed up block sum computation
        for y in range(0, h):
            summation = 0
            
            for x in range(0, w):
                summation += mat[y][x]
                integral_image[y][x] = summation
                
                if y > 0:
                    integral_image[y][x] += integral_image[y-1][x]
        
        
        
        # compute block sum by looking-up integral image
        output_image = [ [ 0 for y in range(w) ] for x in range(h) ]
        
        for y in range(h):
            for x in range(w):
                
                min_row, max_row = max( 0, y-K), min( h-1, y+K)
                min_col, max_col = max( 0, x-K), min( w-1, x+K)
                
                output_image[y][x] = integral_image[max_row][max_col]
                
                if min_row > 0:
                    output_image[y][x] -= integral_image[min_row-1][max_col]
                
                if min_col > 0:
                    output_image[y][x] -= integral_image[max_row][min_col-1]
                    
                if min_col > 0 and min_row > 0:
                    output_image[y][x] += integral_image[min_row-1][min_col-1]
                
        return output_image



# m, n : the dimension of rows and columns of input matrix, mat.

## Time Complexity: O( m * n )
#
# The overhead in time is the nested loops iterating on (y, x), which are of O( m * n ).

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for output matrix, output_image, which is of O( m * n ).


def test_bench():

    test_data = [
                    ([[1,2,3],[4,5,6],[7,8,9]], 0),
                    ([[1,2,3],[4,5,6],[7,8,9]], 1),
                    ([[1,2,3],[4,5,6],[7,8,9]], 2),
                ]

    # expected output:
    '''
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
    [[45, 45, 45], [45, 45, 45], [45, 45, 45]]   
    '''

    for matirx, k in test_data:

        print( Solution().matrixBlockSum(matirx, k) )
    
    return 



if __name__ == '__main__':

    test_bench()