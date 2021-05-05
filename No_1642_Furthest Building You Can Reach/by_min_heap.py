'''

Description:

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.



Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7



Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length

'''


from heapq import heappush, heappop
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        # min-heap to store building gaps
        building_gap_heap = []

        total_buildings = len(heights)

        # scan each building pairs' gap
        for i in range( total_buildings-1 ):

            cur_building_gap = heights[i+1] - heights[i]

            if cur_building_gap > 0:
                # next builidng is height than current one, add to min heap
                heappush(building_gap_heap, cur_building_gap)

            if len(building_gap_heap) > ladders:
                # the number of positive gaps is more than the number of ladders
                # use bricks to fill those smaller gaps

                gap_to_climb = heappop(building_gap_heap)
                bricks -= gap_to_climb

            if bricks < 0:
                # we can not fill more gaps, because the bricks is run out
                return i
            
        # we can reach last building
        return total_buildings-1


# n : the number of heights
# k : the number of building gap

## Time Complexity: O( n log k )
#
# The overhead in time is the cost of iteration, which is of O( n log k )

## Space Complexity: O( k )
#
# The overhead in space is the storage for heap, which is of O( k )

import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().furthestBuilding
        return 

    def test_case_1( self ):

        result = self.solver( heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1 )
        self.assertEqual(result, 4)

    def test_case_2( self ):

        result = self.solver( heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2 )
        self.assertEqual(result, 7)

    def test_case_3( self ):

        result = self.solver( heights = [14,3,19,3], bricks = 17, ladders = 0 )
        self.assertEqual(result, 3)        


if __name__ == '__main__':

    unittest.main()