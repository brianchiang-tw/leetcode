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


Hint #1  

If there're only 2 points, return true.



Hint #2  

Check if all other points lie on the line defined by the first 2 points.



Hint #3  

Use cross product to check collinearity.

'''



from typing import List

from math import gcd

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) == 2:
            # Quick response for simple case
            # Two points must be on the same line
            return True
        
        
        
        
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]
        
        common_factor = gcd(dx, dy)
        dx, dy = dx // common_factor, dy // common_factor
        
        
        size = len( coordinates )
        
        for point_idx in range(2, size ):
            
            delta_x = coordinates[point_idx][0] - coordinates[0][0]
            delta_y = coordinates[point_idx][1] - coordinates[0][1]
            
            common_factor = gcd(delta_x, delta_y)
            delta_x, delta_y = delta_x // common_factor, delta_y // common_factor
            
            if (dx, dy) != (delta_x, delta_y) and (dx, dy) != (-delta_x, -delta_y):
                return False
            
        return True



# n : the length of input list, coordinates.

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of loop, of O( n ), and the cost of gcd, of O( log n ).
# It takes O( n log n ) in total.

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'points')

def test_bench():

    test_data = [
                    TestEntry( points = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] ),
                    TestEntry( points = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]] ),
                    TestEntry( points = [[1,1],[2,2],[-3,-3]] ),
                    TestEntry( points = [[1,1],[2,2],[-3,-4]] ),
                ]        
    
    # expected output:
    '''
    True
    False
    True
    False
    '''

    for t in test_data:

        print( Solution().checkStraightLine( coordinates = t.points) )

    return



if __name__ == '__main__':

    test_bench()