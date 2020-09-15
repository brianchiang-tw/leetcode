'''

Description:

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]



Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].



Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]



Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]



Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105

'''



class Solution:
    def insert(self, intervals, newInterval):
        
        # Constant to help us access start point and end point of interval
        START, END = 0, 1
        
        s, e = newInterval[START], newInterval[END]
        
        left, right = [], []
        
        for cur_interval in intervals:
            
            if cur_interval[END] < s:
                # current interval is on the left-hand side of newInterval
                left += [ cur_interval ]
                
            elif cur_interval[START] > e:
                # current interval is on the right-hand side of newInterval
                right += [ cur_interval ]
                
            else:
                # current interval has overlap with newInterval
                # merge and update boundary
                s = min(s, cur_interval[START])
                e = max(e, cur_interval[END])
                
        return left + [ [s, e] ] + right    


# n : the length of input list, intervals

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().insert( intervals = [[1,3],[6,9]], newInterval = [2,5] )
        self.assertEqual(result, [[1,5],[6,9]] )


    def test_case_2( self ):
    
        result = Solution().insert( intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] )
        self.assertEqual(result, [[1,2],[3,10],[12,16]] )


    def test_case_3( self ):
        
        result = Solution().insert( intervals = [], newInterval = [5,7] )
        self.assertEqual(result, [[5,7]] )


    def test_case_4( self ):
        
        result = Solution().insert( intervals = [[1,5]], newInterval = [2,3] )
        self.assertEqual(result, [[1,5]] )        


    def test_case_5( self ):
        
        result = Solution().insert( intervals = [[1,5]], newInterval = [2,7] )
        self.assertEqual(result, [[1,7]] )     


if __name__ == '__main__':

    unittest.main()