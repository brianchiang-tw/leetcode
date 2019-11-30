'''

Description:

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.

'''

# Allow python feature with type hint
from typing import List

# for defaultdict
from collections import defaultdict

class Solution:

    # member method to compute greatest common factor
    def gcd(self, x, y):
        if y == 0 :
            return x
        else:
            return self.gcd( y, x % y )



    def maxPoints(self, points: List[List[int]]) -> int:
        
        # total number of 2D points
        size = len( points )

        # to sotre the maximum number of colonear 2D points
        max_num_of_points_colinear = 0

        for i in range( size ):
            
            # a hash (python dictionary)
            # key: (x_delta, y_delta)
            # vluae: number of colinear pointer with slope = y_delta / x_delta
            on_the_same_line = defaultdict( int )

            repeated_2D_point = 1

            # get coordinate of 2D Point i
            x_of_point_i = points[i][0]
            y_of_point_i = points[i][1]

            for j in range(i+1, size):

                # get coordinate of 2D Point j
                x_of_point_j = points[j][0]
                y_of_point_j = points[j][1]

                if x_of_point_i == x_of_point_j and y_of_point_i == y_of_point_j:

                    repeated_2D_point += 1
                    continue

                delta_x = x_of_point_i - x_of_point_j
                delta_y = y_of_point_i - y_of_point_j   
                
                # get greatest common factor
                factor = self.gcd( delta_x, delta_y )
                
                # slope = delta_y / delta_x 
                #       = ( delta_y / factor ) / ( delta_x / factor )

                # simplify to irreducible fraction
                delta_x /= factor
                delta_y /= factor

                # update the number of colinear 2D point
                #
                on_the_same_line[(delta_x, delta_y)] += 1

            #print(" on the same line.value() : {}".format( on_the_same_line.values() )  )

            # get the max number of colinear points
            if len( on_the_same_line ) != 0:
                current_max_num_pt_colinear = max( on_the_same_line.values() ) + repeated_2D_point

            else:
                current_max_num_pt_colinear = repeated_2D_point

            #current_max_num_pt_colinear \
            #= ( max( on_the_same_line.values() ) if max_num_of_points_colinear else 0 ) + repeated_2D_point

            # update the global max number of colinear points
            max_num_of_points_colinear \
                = max( max_num_of_points_colinear, current_max_num_pt_colinear)
    
        return max_num_of_points_colinear


## Time Complexity : O( N ^ 2 )
#
# The major workhorse is the outter for loop and inner for loop
# Respectively, outter for loop takes O( N ) and inner for loop takes O( N ), combining together is O( N ^ 2 )

## Space Complexity : O( N )
#
# The overload is the hash( python dictionary ) on_the_same_line, which size is at most O( N )

# on_the_same_line:
# key: (x_delta, y_delta)
# vluae: number of colinear pointer with slope = y_delta / x_delta


def test_bench():


    test_data = [ 
                    [   [1,1],[2,2],[3,3]   ],
                    [   [1,1],[3,2],[5,3],[4,1],[2,3],[1,4] ]    
                ]

    # expected output:
    '''
    3
    4
    '''

    for test in test_data:

        max_num_of_points_colinear = Solution().maxPoints( test )

        print( max_num_of_points_colinear ) 

    return 



if __name__ == '__main__':

    test_bench()