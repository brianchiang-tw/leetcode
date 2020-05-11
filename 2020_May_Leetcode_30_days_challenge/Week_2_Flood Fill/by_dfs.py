'''

Description:

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.



Example 1:

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
   
   
   
Hint #1  

Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.

'''



from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        h, w = len(image), len(image[0])
        
        visited = set()
		
        def dfs( r, c, src_color, new_color):
            
            if r < 0 or c < 0 or r >= h or c >= w or (r,c) in visited or image[r][c] != src_color:
                # Reject for invalid coordination, repeated traversal, or different color
                return
            
            # update color
            image[r][c] = newColor
            
            # mark current coordination as visited
            visited.add( (r,c) )
            
            # DFS to 4-connected neighbors
            dfs( r-1, c, src_color, new_color )
            dfs( r+1, c, src_color, new_color )
            dfs( r, c-1, src_color, new_color )
            dfs( r, c+1, src_color, new_color )
            
        # ---------------------------------------------------------------------------
        
        dfs(sr, sc, src_color = image[sr][sc], new_color = newColor)
        
        return image



# m, n : the dimension of rows and columns of input image.

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of DFS in image, which is of O( m * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for the visited set, which is of O( m * n )

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'image sr sc newColor')

def test_bench():

    test_data = [
                    TestEntry( image =  [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2 ),
                    TestEntry( image =  [[1,1,1],[0,1,0],[1,1,0]], sr = 1, sc = 1, newColor = 2 ),  
                ]

    # expected output:
    '''
    [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    [[2, 2, 2], [0, 2, 0], [2, 2, 0]]
    '''

    for t in test_data:

        print( Solution().floodFill( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()