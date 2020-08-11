'''

Description:

You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:

Choose array nums1 or nums2 to traverse (from index-0).
Traverse the current array from left to right.
If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).
Score is defined as the sum of uniques values in a valid path.

Return the maximum score you can obtain of all possible valid paths.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
Output: 30
Explanation: Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
The maximum is obtained with the path in green [2,4,6,8,10].



Example 2:

Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
Output: 109
Explanation: Maximum sum is obtained with the path [1,3,5,100].



Example 3:

Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
Output: 40
Explanation: There are no common elements between nums1 and nums2.
Maximum sum is obtained with the path [6,7,8,9,10].



Example 4:

Input: nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
Output: 61
 

Constraints:

1 <= nums1.length <= 10^5
1 <= nums2.length <= 10^5
1 <= nums1[i], nums2[i] <= 10^7
nums1 and nums2 are strictly increasing.

'''



from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        size_1, size_2 = len(nums1), len(nums2)
        
        idx_1, idx_2 = 0, 0
        
        cur_acc_1, cur_acc_2 = 0, 0
        
        while idx_1 < size_1 or idx_2 < size_2:
            
            pre_acc_1, pre_acc_2 = cur_acc_1, cur_acc_2
            
            if (idx_1 < size_1 and idx_2 < size_2) and nums1[idx_1] == nums2[idx_2]:
                
                # now we have common number, select the larger branch
                # then update accumulation of list 1 and list 2
                accumulation = max(pre_acc_1, pre_acc_2) + nums1[idx_1] 
                cur_acc_1, cur_acc_2 = accumulation, accumulation
                
                idx_1, idx_2 = idx_1 + 1, idx_2 + 1
                
            elif idx_1 < size_1 and ((idx_2 == size_2) or (nums1[idx_1] < nums2[idx_2])):
                
                # list 2 meet the end or list 1 has smaller element
                # update accumulation of list 1
                cur_acc_1 = pre_acc_1 + nums1[idx_1] 
                idx_1 += 1
                
            elif idx_2 < size_2 and ((idx_1 == size_1) or (nums2[idx_2] < nums1[idx_1])):
                
                # list 1 meet the end or list 2 has smaller element
                # update accumulation of list 2
                cur_acc_2 = pre_acc_2 + nums2[idx_2] 
                idx_2 += 1
                
                
        # remember to module constant before return answer
        return max(cur_acc_1, cur_acc_2) % (10**9 + 7)


# m : the length of nums1
# n : the length of nums2

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of iteration, which is of O( m + n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9])
        self.assertEqual(result, 30)


    def test_case_2( self ):
    
        result = Solution().maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100])
        self.assertEqual(result, 109)


    def test_case_3( self ):
        
        result = Solution().maxSum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10])
        self.assertEqual(result, 40)


    def test_case_4( self ):
        
        result = Solution().maxSum(nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12])
        self.assertEqual(result, 61)


if __name__ == '__main__':

    unittest.main()        