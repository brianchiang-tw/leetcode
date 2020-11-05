'''

Description:

Given an integer array nums, return the number of longest increasing subsequences.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].



Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106

'''


from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        if not nums:
            # Quick response for empty list
            return 0
        
        n = len(nums)
        
        # record of length of increasing subsequence
        length = [1 for _ in range(n)]
        
        # record the path count of increasing subsequence
        count = [1 for _ in range(n)]
            
        # scan each number, where increasing subsequence ending in nums[i]
        for i in range(n):
            
            # for every number before nums[i]
            for j in range(i):
                
                
                if nums[j] < nums[i]:
                    # nums[j] can add to increasing subsequence ending in nums[i]
                    
                    if (length[j] + 1) > length[i]:
                        # nums[j] make it longer to increasing subsequence ending in nums[i]
                        length[i], count[i] = length[j]+1, count[j]
                
                    elif (length[j] + 1) == length[i]:
                        # nums[j] add some new paths of increasing subsequence ending in nums[i]
                        count[i] += count[j]
        
        
        max_length = max(length)
        
        # report total path count of longest increasing subsequence
        return sum( count for length, count in zip(length, count) if length == max_length )


# n : the length of nums

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of nested for-loops, which is of O( n^2 )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findNumberOfLIS( nums=[1,3,5,4,7] )
        self.assertEqual(result, 2)


    def test_case_2( self ):

        result = Solution().findNumberOfLIS( nums=[2,2,2,2,2] )
        self.assertEqual(result, 5)


if __name__ == '__main__':

    unittest.main()
    