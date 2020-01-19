'''

Description:

A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true



Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
 

Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
 

'''



from typing import List
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        #x1, y1 = points[0]
        #x2, y2 = points[1]
        #x3, y3 = points[2]
        
        # if any two of them are identical, then three points are co-linear
        # if three points are co-linear, then reject
        
        # the triangle area enclosed by three points is zero if and only if three points are co-linear.
        determinant = (points[0][0]-points[1][0]) * (points[1][1]-points[2][1]) - (points[0][1]-points[1][1]) * (points[1][0]-points[2][0])
        
        if determinant == 0:
            return False
        
        return True



# Time Complexity: O( 1 )
#
# The overhead in time is the computation of determinant, which is of O( 1 ).

## Space Complexity: O( 1 )
#
# The overhead in space is the variable for computation, which is of O( 1 ).



def test_bench():

    test_data = [
                    [[1,1],[2,3],[3,2]],
                    [[1,1],[2,2],[3,3]],
                    [[1,1],[2,4],[3,5]]
                ]

    # expected output:
    '''
    True
    False
    True    
    '''

    for triset_of_points in test_data:

        print( Solution().isBoomerang(triset_of_points) )
    
    return 



if __name__ == '__main__':

    test_bench()