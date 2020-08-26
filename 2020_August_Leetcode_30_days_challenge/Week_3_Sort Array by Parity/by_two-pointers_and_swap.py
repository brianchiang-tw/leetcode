'''

Description:

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

'''


from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        # ------------------------------------------------
        def swap(arr, odd_idx ):
            
            arr[swap.even_idx], arr[odd_idx] = arr[odd_idx], arr[swap.even_idx]
            swap.even_idx += 1
        
        # ------------------------------------------------
        
        swap.even_idx = 0
        
        is_even_number = lambda x: not( x & 1 )
        
        for i in range( len(A) ):
            # scan each element
            
            if is_even_number(A[i]): swap(A, i)
            # swap even number to the left-hand side
            
        return A



# n : the length of input array, A

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        res = Solution().sortArrayByParity( A = [3,1,2,4] )
        check_even = all( map(lambda x: x%2 == 0, res[:len(res)//2] ) )
        self.assertEqual(check_even, True)


    def test_case_2( self ):

        res = Solution().sortArrayByParity( A = [7,1,2,5,6,8] )
        check_even = all( map(lambda x: x%2 == 0, res[:len(res)//2] ) )
        self.assertEqual(check_even, True)


if __name__ == '__main__':

    unittest.main()