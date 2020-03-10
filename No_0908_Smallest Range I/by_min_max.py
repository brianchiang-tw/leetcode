'''

Description:

Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]



Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]



Example 3:

Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]
 

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000

'''


from typing import List
from collections import namedtuple

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:

        M, m = max(A), min(A)
        diff, extension = M - m, 2*K
        
        if diff <= extension:
            return 0
        
        else:
            return diff - extension



# n : the length of input list A 

## Time Complexity: O( n )
#
# The overhead in time is the cost of min(A) as well as max(A), which are of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 ).


TestEntry = namedtuple('TestEntry', 'A K')
def test_bench():

    test_data = [
                    TestEntry( A = [1], K = 0 ),
                    TestEntry( A = [0,10], K = 2 ),
                    TestEntry( A = [1,3,6], K = 3 ),
                ]

    for t in test_data:

        print( Solution().smallestRangeI( A = t.A, K = t.K ) )

    return



if __name__ == '__main__':

    test_bench()