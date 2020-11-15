'''

Description:

Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true



Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false



Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
 

Constraints:

p1.length == p2.length == p3.length == p4.length == 2
-104 <= xi, yi <= 104

'''



from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        point = [p1, p2, p3, p4]
        
        edge_length = set()
        
        # lambda to compute edge length between point pair
        get_length = lambda a, b: ( (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 ) ** 0.5
        
        # check each point pair
        for i in range(3):
            for j in range(i+1,4):
                
                cur_length = get_length(point[i], point[j])
                
                if cur_length == 0:
                    # Reject when any two points are repeated
                    return False
                
                edge_length.add( cur_length )
                

        # Accept if only two kinds of edges length, one is side length, the other is diagonal length
        return len(edge_length) == 2


## Time Complexity: O( 1 )
#
# The overhead in time is the cost of point pair checking, which is of O( C(4, 2) ) = O( 6 ) = O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().validSquare( p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1] )
        self.assertEqual(result, True)

    
    def test_case_2( self ):

        result = Solution().validSquare( p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12] )
        self.assertEqual(result, False)


    def test_case_3( self ):

        result = Solution().validSquare( p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1] )
        self.assertEqual(result, True)


if __name__ == '__main__':

    unittest.main()