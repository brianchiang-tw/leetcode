'''

Description:

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.



Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.

'''

from typing import List

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        
        global_inversion, local_inversion = 0, 0
        
        size = len(A)
        
        for cur_idx, cur_num in enumerate(A):
            
            ## for global inversion
            if cur_num > cur_idx:
                
                # current number is too big, update with the count of mismatch on smaller elements
                global_inversion += cur_num - cur_idx
                
            elif cur_num < cur_idx:
                
                # current number is too small, update with the count of mismatch on larger elements
                global_inversion += cur_idx - cur_num - 1
                
            
            ## for local inversion
            if (cur_idx < size-1) and (A[cur_idx] > A[cur_idx+1]):
                
                # current number is out of order, update with current mismatch pair
                local_inversion += 1
        
        
        return global_inversion == local_inversion


# n : the length of input list A

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:

        self.solver = Solution().isIdealPermutation
        return 

    def test_case_1( self ):

        result = self.solver( A = [1,0,2] )
        self.assertEqual(result, True)



    def test_case_2( self ):

        result = self.solver( A = [1,2,0] )
        self.assertEqual(result, False)

