'''

Description:

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

'''



from typing import List
from math import floor
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        
        
        rows, cols = len(M), len(M[0])
        
        output = [ [ 0 for i in range(cols) ] for j in range(rows) ]
        
        
        for y in range( rows ):
            for x in range( cols ) :
                
                neighbor_pixels = []
                
                for offset_y in range(-1,2,1):
                    for offset_x in range(-1,2,1):
                        
                        ny = y + offset_y
                        nx = x + offset_x
                        
                        if rows > ny >= 0 and cols > nx >= 0:
                            neighbor_pixels.append( M[ny][nx] )
                            
                output[y][x] = floor( sum(neighbor_pixels) / len(neighbor_pixels) )
                
        return output



# m, n : dimension of rows and columns of input image, M.

## Time Complexity: O( m * n )
#
# The overhead in time is the nested loops, which is of O( m * n * 3 * 3) = O( 9 * m * n ) = O( m * n)


## Space Complexity: O( m * n )
#
# The overhead in space is the storage for output image matrix, which is of O( m * n)




def test_bench():

    test_data = [
                    [[1,1,1],
                    [1,0,1],
                    [1,1,1]],

                    [[1,2,3],
                    [4,5,6],
                    [7,8,9]]
                ]

    # expected output:
    '''
    [[0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]]

    [[3, 3, 4], 
    [4, 5, 5], 
    [6, 6, 7]]
    '''


    for image_matrix in test_data:

        print( Solution().imageSmoother(image_matrix) )
    
    return 



if __name__ == '__main__':

    test_bench()