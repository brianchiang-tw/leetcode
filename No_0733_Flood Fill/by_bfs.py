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

'''



from typing import List
from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        h, w = len(image), len(image[0])
        
        src_color = image[sr][sc]
        
        visited = set()
        
        traversal_queue = deque( [(sr, sc)] )
        
        while traversal_queue:
            
            cur_r, cur_c = traversal_queue.popleft()
            
            if cur_r < 0 or cur_r >= h or cur_c < 0 or cur_c >= w or (cur_r, cur_c) in visited or image[cur_r][cur_c] != src_color:
                continue
            
            # update color
            image[cur_r][cur_c] = newColor
            
            # mark current coordinate as visited
            visited.add( (cur_r, cur_c) )
            
            # BFS to 4-connected neighbors
            traversal_queue.append( (cur_r-1, cur_c) )
            traversal_queue.append( (cur_r+1, cur_c) )
            traversal_queue.append( (cur_r, cur_c-1) )
            traversal_queue.append( (cur_r, cur_c+1) )
        
        return image



# m, n : the dimension of rows and columns of image

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of BFS traversal, which is of O( m*n )

## Space Complexity: O( m*n )
#
# The overhead in space is the storage for visited set, which is of O( m*n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'image sr sc new_color')


def test_bench():

    test_data = [
                    TestEntry( image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, new_color = 2 ),
                    TestEntry( image = [[1,1,1],[0,1,0],[0,1,1]], sr = 1, sc = 1, new_color = 2 ),
                ]

    # expected output:
    '''
    [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    [[2, 2, 2], [0, 2, 0], [0, 2, 2]]
    '''

    for t in test_data:

        Solution().floodFill( *t )

        print( t.image )
    
    return




if __name__ == '__main__':

    test_bench()    