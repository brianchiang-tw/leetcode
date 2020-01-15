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
        
        # check for y = mx + b on slope m = delta y / delta x
        try:
            slope = (y_1 - y_0) / (x_1 - x_0)
            if all( [ ( (coordinates[i][1]-y_0) / (coordinates[i][0]-x_0) ) == slope  for i in range( 1, len( coordinates ) ) ] ):
                return True
        except:
            # non-colinear
            # zero division where some x_i == x_0
            return False
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