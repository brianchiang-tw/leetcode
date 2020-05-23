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
# The overhead in time is the cost of linear scan, which is of O( m + n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )

def test_bench():

    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]

    # expected output:
    '''
    [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    '''
    print( Solution().intervalIntersection( A, B) )

    # ----------------------------------------------------

    A = [[0,5]]
    B = [[3,7]]

    # expected output:
    '''
    [[3, 5]]
    '''
    print( Solution().intervalIntersection( A, B) )

    return



if __name__ == '__main__':

    test_bench()