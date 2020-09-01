'''

Description:

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
 

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
 

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''



from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):

        START, END = 0, 1
        
        # sort on pairs in ascending order
        # pair: ( START position of interval, original index)
        start_and_idx_pairs = sorted( (interval[START], idx) for idx, interval in enumerate(intervals) )

        result = []

        for interval in intervals:
            
            # get the index of first larger pair
            idx_of_first_larger_pair = bisect_left(start_and_idx_pairs, (interval[END],) )
            
            # original index of right interval before sorting, initialized as -1    
            idx_of_right_interval = -1
            
            if idx_of_first_larger_pair < len(intervals):
                # if the index of first larger pair exists, get original index before sorting    
                idx_of_right_interval = start_and_idx_pairs[idx_of_first_larger_pair][1]

            result.append( idx_of_right_interval )
            
        return result



# n : the length of intervals

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for result output, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):
        result = Solution().findRightInterval( intervals=[ [1,2] ] )
        self.assertEqual( result, [-1] )
        

    def test_case_2( self ):
        result = Solution().findRightInterval( intervals=[ [3,4], [2,3], [1,2] ] )
        self.assertEqual( result, [-1, 0, 1] )


    def test_case_3( self ):
        result = Solution().findRightInterval( intervals=[ [1,4], [2,3], [3,4] ] )
        self.assertEqual( result, [-1, 2, -1] )


if __name__ == '__main__':

    unittest.main()