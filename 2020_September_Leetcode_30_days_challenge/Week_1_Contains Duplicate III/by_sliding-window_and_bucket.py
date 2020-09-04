'''

Description:

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true



Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true



Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
 

Constraints:

0 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^4
0 <= t <= 2^31 - 1

'''


from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if t == 0 and len(set(nums)) == len(nums):
            
            # Quick response for t = 0
            # t = 0 requires at least one pair of repeated element
            
            return False
            
        
        size = len(nums)
        
        bucket = {}
        
        width = t + 1
        
        for idx, number in enumerate(nums):
            
            bucket_idx = number // width
            
            if bucket_idx in bucket:
                
                # two numbers in the same bucket, gap must be smaller than width
                return True
            
            elif bucket_idx + 1 in bucket and abs(number - bucket[bucket_idx + 1]) < width:
                
                # two number in two consecutive buckets, and gap is smaller than width
                return True
            
            elif bucket_idx - 1 in bucket and abs(number - bucket[bucket_idx - 1]) < width:
                
                # two number in two consecutive buckets, and gap is smaller than width
                return True
            
            # put current number into corresponding bucket
            bucket[bucket_idx] = number
            
            
            if idx >= k:
                
                # delete old number whose index distance larger than k
                del bucket[ nums[idx-k] //width ]
                
        return False



# n : the length of input nums
# k : the value of input parameter k

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( k )
#
# The overhead in space is the storage for dictionary, which is of O( k )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().containsNearbyAlmostDuplicate( nums=[1,2,3,1], k=3, t=0 )
        self.assertEqual(result, True)


    def test_case_2( self ):

        result = Solution().containsNearbyAlmostDuplicate( nums=[1,0,1,1], k=1, t=2 )
        self.assertEqual(result, True)


    def test_case_3( self ):

        result = Solution().containsNearbyAlmostDuplicate( nums=[1,5,9,1,5,9], k=2, t=3 )
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()