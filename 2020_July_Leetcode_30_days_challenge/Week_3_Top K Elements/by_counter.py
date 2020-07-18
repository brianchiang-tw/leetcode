'''

Description:

Given a non-empty array of integers, return the k most frequent elements.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]



Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

'''



from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return [number for number, occ in Counter(nums).most_common(k)]



# n : the length of input list, nums.

## Time Complexity: O( n log k )
#
# The overhead in time is the cost of most_common(k), which is of O( n log k )


## Space Complexity:　O( n )
#
# The overhead in space is the storage for Counter(nums), which is of O( n )



import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)
        self.assertEqual(result, [1, 2])

    
    def test_case_2( self ):

        result = Solution().topKFrequent(nums = [1], k = 1)
        self.assertEqual(result, [1])



if __name__ == '__main__':

    unittest.main()