'''

Description:

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''



from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        idx_a, idx_b = 0, 0
        size_a, size_b = len(A), len(B)
        
        intersection = []
        
        # Scan each possible interval pair
        while idx_a < size_a and idx_b < size_b :
            
            # Get start-time as well as end-time
            start_a, end_a = A[idx_a]
            start_b, end_b = B[idx_b]
            
            
            # Compute common start time and end time for current interval pair
            common_start = max( start_a, start_b )
            common_end = min( end_a, end_b )
            
            if common_start <= common_end:
                # Find one common overlapped interval
                intersection.append( [common_start, common_end] )
                
            if end_a <= end_b:
                # Try next interval of A
                idx_a += 1
                
            else:
                # Try next interval of B
                idx_b += 1
        
        return intersection


# m : the length of input list A
# n : the length of input list B

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of linear iteration, which is of O( m + n )

## Space Complexity: O( m + n )
#
# The overhae in space is the list of intersection output list, which is of O( m + n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'A B')
def test_bench():

    test_data = [
                    TestEntry( A = [[0,2],[5,10],[13,23],[24,25]] , B = [[1,5],[8,12],[15,24],[25,26]] ),
                    TestEntry( A = [[0,5]] , B = [[1,3]]),
                    TestEntry( A = [[5,10]] , B = [[8,12]]),
                    TestEntry( A = [[5,10]] , B = [[10,12]]),
                ]

    # expected output:
    '''
    [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    [[1, 3]]
    [[8, 10]]
    [[10, 10]]
    '''

    for t in test_data:

        print( Solution().intervalIntersection( *t) )
    
    return



if __name__ == '__main__':

    test_bench()
