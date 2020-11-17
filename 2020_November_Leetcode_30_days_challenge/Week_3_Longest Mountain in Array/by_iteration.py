'''

Description:

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.



Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.



Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?

'''



'''        
class Solution:
    def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)
        return res
        
'''


class Solution:
    def longestMountain(self, A):

        maximum = 0
        go_up = 0
        go_down = 0
        
        for idx in range(1, len(A)):
            
            if (go_down and A[idx-1] < A[idx]) or A[idx-1] == A[idx]:
                # reset after boundary of current mountain is found
                go_up = 0
                go_down = 0
                
            if A[idx-1] < A[idx]:
                # current height is higher than previous one
                go_up += 1
            
            if A[idx-1] > A[idx]:
                # current height is lower than pervious one
                go_down += 1
                
            if go_up and go_down:
                # update with length of current mountain
                maximum = max( maximum, go_up + go_down + 1 )
                
        return maximum



# n : the length of array

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().longestMountain( A=[2,1,4,7,3,2,5] )
        self.assertEqual(result, 5)


    def test_case_2( self ):

        result = Solution().longestMountain( A=[2,2,2] )
        self.assertEqual(result, 0)
    