'''

Description:

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.

'''



from typing import List
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        size = len(points)
        max_area_of_parallelogram = 0
        
        # Choose 3 points on iteration
        for i  in range( size):
            for j in range( i+1, size):
                for k in range( j+1, size):
                    
                    # point A:
                    point_a_x, point_a_y = points[i] 
                    
                    # point B:
                    point_b_x, point_b_y = points[j]
                    
                    # point C:
                    point_c_x, point_c_y = points[k]
                    
                    # compute the area of parallelogram, composed by vector AB and AC
                    cur_area = abs( point_a_x * point_b_y + \
                                    point_b_x * point_c_y + \
                                    point_c_x * point_a_y - \
                                    point_a_x * point_c_y - \
                                    point_b_x * point_a_y - \
                                    point_c_x * point_b_y )
                    
                    # update maximum area of parallelogram
                    max_area_of_parallelogram = max(max_area_of_parallelogram, cur_area)
        
        # max area of triangle = max area of parallelogram / 2
        return max_area_of_parallelogram / 2



# n : the length of input array, points.

## Time Complexity: O( n ^ 3 )
#
# The overhead in time is the cost of triple nested loops, iterating up to n, which is of O( n^3 ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index, and temporary area computing variable, which is of O( 1 ).


def test_bench():

    test_data = [
                    [[0,0],[0,1],[1,0],[0,2],[2,0]]
                ]

    for points in test_data:

        print( Solution().largestTriangleArea(points) )
    
    return 



if __name__ == '__main__':

    test_bench()