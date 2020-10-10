'''

Description:

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.



Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).



Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).



Example 4:

Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2



Example 5:

Input: nums = [-1,-2,-3], k = 1
Output: 2
 

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107

'''


from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        ## dictionary
        # key: unique number
        # value: occurrence
        unique_num = Counter(nums)
        
        count = 0
        
        for x in unique_num:
            
            if k and x + k in unique_num:
                # case with k != 0
                # both x and x + k exist
                count += 1
            
            elif not k and unique_num.get(x+k, 0) >= 2:
                # case k == 0
                # x exists at least two time
                count += 1
                
        return count



# n : the length of nums

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( n )
#
# The ovehread in space is the storage for dictionary, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findPairs( nums = [3,1,4,1,5], k = 2 )
        self.assertEqual(result, 2)

    
    def test_case_2( self ):

        result = Solution().findPairs( nums = [1,2,3,4,5], k = 1 )
        self.assertEqual(result, 4)


    def test_case_3( self ):

        result = Solution().findPairs( nums = [1,3,1,5,4], k = 0 )
        self.assertEqual(result, 1)



if __name__ == '__main__':

    unittest.main()        

