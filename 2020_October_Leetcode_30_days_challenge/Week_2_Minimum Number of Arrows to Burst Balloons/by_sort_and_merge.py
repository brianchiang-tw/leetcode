'''

Description

There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).



Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4



Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2



Example 4:

Input: points = [[1,2]]
Output: 1



Example 5:

Input: points = [[2,3],[2,3]]
Output: 1
 

Constraints:

0 <= points.length <= 104
points.length == 2
-231 <= xstart < xend <= 231 - 1

'''


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        
        if not points:
            # Quick response for zero ballon
            return 0
        
        START, END = 0, 1
        
        # sort by start-index and end-index
        points.sort( key=lambda p:(p[START], p[END]) ) 
        
        # initialization for arrow
        arrow_shot = len(points)
        
        # initialization for coverage
        cur_coverage = points[0]
        
        # check for interval overlapping
        for interval in points[1:]:
            
            if interval[START] <= cur_coverage[END]:
                # overlap with current coverage
                # merge with cur_coverage
                cur_coverage = [ max(cur_coverage[START], interval[START]), min(cur_coverage[END], interval[END]) ]
                
                arrow_shot -= 1 
                
            else:
                # no overlap
                # update interval as cur_coverage
                cur_coverage = interval
        
        return arrow_shot


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findMinArrowShots( points = [[10,16],[2,8],[1,6],[7,12]] )
        self.assertEqual(result, 2)


    def test_case_2( self ):

        result = Solution().findMinArrowShots( points = [[1,2],[3,4],[5,6],[7,8]] )
        self.assertEqual(result, 4)        


    def test_case_3( self ):

        result = Solution().findMinArrowShots( points = [[1,2],[2,3],[3,4],[4,5]] )
        self.assertEqual(result, 2)  


    def test_case_4( self ):

        result = Solution().findMinArrowShots( points = [[1,2]] )
        self.assertEqual(result, 1)  


    def test_case_5( self ):

        result = Solution().findMinArrowShots( points = [[2,3],[2,3]] )
        self.assertEqual(result, 1)  


    def test_case_6( self ):

        result = Solution().findMinArrowShots( points = [] )
        self.assertEqual(result, 0)  


if __name__ == '__main__':

    unittest.main()        