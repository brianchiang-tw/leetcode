'''

Description:

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.



Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1



Example 3:

Input: intervals = [[0,10],[5,12]]
Output: 2



Example 4:

Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2



Example 5:

Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= intervals[i][0] < intervals[i][1] <= 10^5
All the intervals are unique.

'''



from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        START, END = 0, 1
        
        # Sort by left bound, and reversed right bound of interval
        intervals.sort(key=lambda segment:(segment[0], -segment[1]) )
        
        # count of non-covered intervals
        count = 0
        
		# right bound so far
        right_bound = 0
        
        for interval in intervals:
            
            if right_bound < interval[END]:
                # previous interval can not cover current interval, update count
                count, right_bound = count+1, interval[END]
                
        return count


# n : the length of intervals

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().removeCoveredIntervals( intervals=[[1,4],[3,6],[2,8]] )
        self.assertEqual(result, 2)


    def test_case_2( self ):

        result = Solution().removeCoveredIntervals( intervals=[[1,4],[2,3]] )
        self.assertEqual(result, 1)


    def test_case_3( self ):

        result = Solution().removeCoveredIntervals( intervals=[[0,10],[5,12]] )
        self.assertEqual(result, 2)        


    def test_case_4( self ):

        result = Solution().removeCoveredIntervals( intervals=[[3,10],[4,10],[5,11]] )
        self.assertEqual(result, 2)


    def test_case_5( self ):

        result = Solution().removeCoveredIntervals( intervals=[[1,2],[1,4],[3,4]] )
        self.assertEqual(result, 1)


if __name__ == '__main__':

    unittest.main()        