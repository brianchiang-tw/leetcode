'''

Description:

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.



Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.



Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

'''


from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        # sort segments by start index in ascending order
        intervals.sort( key = lambda segment: segment[0] )
        
        last_compare_idx = 0
        removal_counter = 0
   

        for cur_idx in range(1, len(intervals)):
            
            cur_start, cur_end = intervals[cur_idx]
            last_start, last_end = intervals[last_compare_idx]
            
            
            if cur_start < last_end:
                
                # need to remove one interval to avoid overlapping
                removal_counter += 1
                
                if cur_end < last_end:
                    
                    # remove last interval, because it is lefter then current
                    last_compare_idx = cur_idx
                
                else:
                    
                    # remove current interval, because it is lefter then last one
                    # last compare idx keeps the same
                    pass
                    
            else:
                # so far so good, no need to remove
                last_compare_idx = cur_idx
        
        return removal_counter


# n : the length of input list, intervals

## Time Complexity: O( n log n)
#
# The overhead in time is the cost of sorting, which is of O( n log n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().eraseOverlapIntervals( intervals=[[1,2],[2,3],[3,4],[1,3]] )
        self.assertEqual(result, 1)


    def test_case_2( self ):

        result = Solution().eraseOverlapIntervals( intervals=[[1,2],[1,2],[1,2]] )
        self.assertEqual(result, 2)


    def test_case_3( self ):

        result = Solution().eraseOverlapIntervals( intervals=[[1,2],[2,3]] )
        self.assertEqual(result, 0)



if __name__ == '__main__':

    unittest.main()