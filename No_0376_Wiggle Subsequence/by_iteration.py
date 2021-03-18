'''

Description

Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.



Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].



Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000

'''

from typing import List

class Solution(object):

    def wiggleMaxLength( self, nums: List[int]):

        n = len( nums )

        # length of wiggle sequence, ending in positive dfference, negative difference
        positive, negative = 1, 1

        # scan from seond number to last number
        for i in range(1, n):

            if nums[i] > nums[i-1]:

                # difference is positive, concatenated with negative prefix wiggle subsequence
                positive = negative + 1

            elif nums[i] < nums[i-1]:

                # difference is negative, concatenated with positive prefix wiggle subsequence
                negative = positive + 1
            
        
        # compute the longest length of wiggle sequence
        return max(positive, negative)



# n : the length of input nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().wiggleMaxLength( nums = [1,7,4,9,2,5] )
        self.assertEqual(result, 6)

    
    def test_case_2( self ):

        result = Solution().wiggleMaxLength( nums = [1,17,5,10,13,15,10,5,16,8] )
        self.assertEqual(result, 7)


    def test_case_3( self ):

        result = Solution().wiggleMaxLength( nums = [1,2,3,4,5,6,7,8,9] )
        self.assertEqual(result, 2)


if __name__ == '__main__':

    unittest.main()        