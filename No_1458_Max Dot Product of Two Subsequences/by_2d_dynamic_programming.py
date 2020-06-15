'''

Description:

Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.



Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.



Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.
 

Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000

'''



from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        # add one dummy zero as empty sequence
        nums1 = [0] + nums1
        nums2 = [0] + nums2
        
        
        h, w = len(nums1), len(nums2)
        
        # initialization as -∞
        dp_table = [ [ float('-inf') for _ in range(w)] for _ in range(h) ]
        
        
        # Solve dy 2D dynamic programming with optimal substructure
        for y in range(1,h):
            for x in range(1, w):
                
                # compute current dot product of nums1[y] and nums2[x]
                current_product = nums1[y] * nums2[x]
                
                if current_product > 0:
                    
                    # current product is positive
                    # update with four candidate:
                    dp_table[y][x] = max(dp_table[y-1][x-1] + current_product, current_product, dp_table[y-1][x], dp_table[y][x-1])
                                        
                        
                else:
                    
                    # current product is negative
                    # update with three candidate
                    dp_table[y][x] = max(dp_table[y-1][x], dp_table[y][x-1], current_product)
                    

        return dp_table[-1][-1]



# m : the length of nums1
# n : the length of nums2



## Time Complexity: O( m * n )
#
# The overhead in time is the cost of 2d dynamic programming, which is of O( m * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for table of dynamic programming, which is of O( m * n )


import unittest
from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'nums1 nums2')



class Testing(unittest.TestCase):

    def test_case_1(self):

        t = TestEntry( nums1 = [2, 1, -2, 5], nums2 = [3, 0, -6] )
        result = Solution().maxDotProduct( *t )

        # expected output: 18
        self.assertEqual( result, 18)


    def test_case_2(self):
        
        t = TestEntry( nums1 = [3, -2], nums2 = [2, -6, 7] )
        result = Solution().maxDotProduct( *t )
        
        # expected output: 21
        self.assertEqual( result, 21)


    def test_case_3(self):

        t = TestEntry( nums1 = [-1 ,-1], nums2 = [1, 1] )
        result = Solution().maxDotProduct( *t )

        # expected output: -1
        self.assertEqual( result, -1)


    def test_case_4(self):
    
        t = TestEntry( nums1 = [5 ,-4, -3], nums2 = [-4, -3, 0, -4, 2] )
        result = Solution().maxDotProduct( *t )

        # expected output: 28
        self.assertEqual( result, 28)


if __name__ == '__main__':

    unittest.main()