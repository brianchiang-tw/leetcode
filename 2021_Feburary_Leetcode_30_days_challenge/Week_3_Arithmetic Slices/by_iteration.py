'''

Description:

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.



Example 2:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000

'''


from typing import List

class Solution():

    def numberOfArithmeticSlices(self, A:List[int]):

        slice_count = 0
        cur_combination = 0
        last_difference = 0

        size = len(A)

        if size < 3:

            # array size if too small, no chance to have arithmetic slices
            return 0

        
        # scan each element pair in order
        for i in range(size-1):

            # compute current difference of element pair
            cur_difference = A[i+1] - A[i]

            if i and cur_difference == last_difference:

                # arithmetic slice is met
                cur_combination += 1

                # update slice count
                slice_count += cur_combination
            
            else:

                # difference is changed, reset current combination
                cur_combination = 0

        
            # update last difference as current difference
            last_difference = cur_difference

        return slice_count


## n : the length of input list A

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().numberOfArithmeticSlices( A=[1,2,3,4] )
        self.assertEqual(result, 3)

    
    def test_case_2( self ):

        result = Solution().numberOfArithmeticSlices( A=[1] )
        self.assertEqual(result, 0)

    

if __name__ == '__main__':

    unittest.main()