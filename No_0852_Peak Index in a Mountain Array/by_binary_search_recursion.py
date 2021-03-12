'''

Description:

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

'''



from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        def helper(arr, left, right):
            
            if right == left:
                # base case
                return left
            
            # general case with binary search core
            mid = left + (right - left) // 2
            
            if ( arr[mid-1] < arr[mid] ) and ( arr[mid] > arr[mid+1] ):
                
                # hit, directly get peak
                return mid
            
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                
                # current direction is uphill, so peak is on the right hand side
                return helper( arr, mid, right)     
            
            else:
                # current direction is downhill, so peak is on the left hand side
                return helper( arr, left, mid)     
            
            
        # -------------------------------------------
        size = len(arr)
        return helper(arr, left=0, right=size-1)



# n : the length of mountain array

## Time Complexity: O( log n )
#
# The overhead in time is the cost of binary search of a list of n, which is of O( n )

## Space Complexity: O( log n )
#
# The overhead in space is the storage for recursion call stack, which is of O( log n )


import unittest

class Testing( unittest.TestCase):

    def test_case_1( self ):

        result = Solution().peakIndexInMountainArray( arr=[1,2,3,4,5,3,1] )
        self.assertEqual(result, 4)


    def test_case_2( self ):

        result = Solution().peakIndexInMountainArray( arr= [0,1,2,4,2,1] )
        self.assertEqual(result, 3)


    def test_case_3( self ):

        result = Solution().peakIndexInMountainArray( arr= [1,2,3,4,5,3,1] )
        self.assertEqual(result, 4)


    def test_case_4( self ):

        result = Solution().peakIndexInMountainArray( arr= [1,5,2] )
        self.assertEqual(result, 1)


    def test_case_5( self ):

        result = Solution().peakIndexInMountainArray( arr= [1,2,3,5,3] )
        self.assertEqual(result, 3)        


if __name__ == '__main__':

    unittest.main()
