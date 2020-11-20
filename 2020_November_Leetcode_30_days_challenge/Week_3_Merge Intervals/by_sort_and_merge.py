'''

Description:

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].



Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

'''



from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # predefined constant for start (left endpoint), and end (right endpoint)
        START, END = 0, 1
        
        result = []
        
        # make all intervals sorted on (left endpoint, right endpoint) pair in ascending order
        intervals.sort( key = lambda x: (x[START], x[END] ) ) 
        
        for interval in intervals:
            
            if not result or ( result[-1][END] < interval[START] ):
				# no overlapping
                result.append( interval )
            
            else:
				# has overlapping
				# merge with previous interval
                result[-1][END] = max(result[-1][END], interval[END])
                
        return result


# n : the length of array intervals:

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for result, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().merge( intervals = [[1,3],[2,6],[8,10],[15,18]] )
        self.assertEqual(result, [[1,6],[8,10],[15,18]] )


    def test_case_2( self ):

        result = Solution().merge( intervals = [[1,4],[4,5]] )
        self.assertEqual(result, [[1,5]] )         


if __name__ == '__main__':

    unittest.main()