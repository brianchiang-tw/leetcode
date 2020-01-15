'''

Description:

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true



Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false



Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

'''



from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        
        if len(coordinates) == 2:
            # Quick response:
            # 2 points must be co-linear
            return True
        
        
        # get first coordinate        
        x_0 = coordinates[0][0]
        y_0 = coordinates[0][1]
        
        
        # check for horizontal line on y-axix value
        if all( [ coord[1] == y_0 for coord in coordinates ] ):
            return True
        
        # check for vertical line on x-axis value
        if all( [ coord[0] == x_0 for coord in coordinates ] ):
            return True
        
        
        
        # get second coordinate
        x_1 = coordinates[1][0]
        y_1 = coordinates[1][1]
        
        
        diff_x_0_1 = x_0 - x_1
        diff_y_0_1 = y_0 - y_1
        
        # triangle area of point A, B, C
        # 
        #           | x_A - x_B    x_B - x_C |
        # = (1/2) * |                        |
        #           | y_A - y_B    y_B - y_C |
        #
        # if det(Area) = 0, then point A, B, C are co-linear 

        # lambda to compute det(Area):
        det_of_area = lambda diff_x_1_2, diff_y_1_2: ( diff_x_0_1*diff_y_1_2 - diff_x_1_2*diff_y_0_1 )
        
        # check for area formed by point_#0, point_#1 and point_#i is 0
        if all( [ det_of_area( x_1 - coordinates[i][0] , y_1 - coordinates[i][1] ) == 0  for i in range( 2, len( coordinates ) ) ] ):
            # co-linear
            return True

        else:
            # non-colinear
            return False



# n : the number of coordinate pair in input

## Time Complexity: O( n )
#
# The overhead in time is those callings of all( ... ) with list comprehension, which are of O( n ).

## Space Complexity: O( n )
# 
# The overhead in space is the storage for those temp object created in list comprehension, which is of O( n ). 



def test_bench():

    test_data = [
                    [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],
                    [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
                ]

    # expected output:
    '''
    True
    False
    '''

    for list_of_coordinate in test_data:

        print( Solution().checkStraightLine(list_of_coordinate) )

    return 



if __name__ == '__main__':

    test_bench()