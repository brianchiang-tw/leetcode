'''

Description:

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Example 1:


Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2



Example 2:

Input: wall = [[1],[1],[1]]
Output: 3
 

Constraints:

n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
sum(wall[i]) is the same for each row i.
1 <= wall[i][j] <= 231 - 1

'''


from typing import  List
from collections import defaultdict

class Solution:

    def leastBrick(self, wall: List[List[int]]) -> int:

        ## dictionary
        # key: boundary
        # value: occurrence of boundary

        boundary_occ_dict = defaultdict(int)

        bricks_rows = len(wall)

        # scan each brick row
        for cur_brick_row in wall:

            # reset current boundary to zero
            cur_boundary = 0

            # update boundary into dictionary
            # Take care that final boundary is excluded to satisfy definition
            for cur_brick_length in cur_brick_row[:-1]:

                cur_boundary += cur_brick_length

                boundary_occ_dict[ cur_boundary ] += 1

        # get occurrence of boundary
        boundary_occurrence = boundary_occ_dict.values()

        # compute minimal crossing by occurrence of boundary

        if boundary_occurrence:
            
            # general cases: multiple bricks on each row
            min_crossing = bricks_rows - max(boundary_occurrence)

        else:

            # corner case: only one brick on each row
            min_crossing = bricks_rows

        return min_crossing


# m : the height of brick wall
# n : the average of bricks on each row

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of iteration, which is of O( m * n )

## Space Complexity: O( n )
#
# The overhead in space is the stroage of dictionary, which is of O( n )

import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().leastBrick
        return

    def test_case_1( self ):
        result = self.solver(  wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]] )
        self.assertEqual(result, 2)

    def test_case_2( self ):
        result = self.solver(  wall = [[1],[1],[1]] )
        self.assertEqual(result, 3)


if __name__ == '__main__':

    unittest.main()