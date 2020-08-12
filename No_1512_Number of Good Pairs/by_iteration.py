'''

Description:

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.



Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

'''


from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        good_pair_count = 0
        
        for i in range(size - 1):
            
            for j in range(i+1, size):
                
                if nums[i] == nums[j]:
                    good_pair_count += 1
                    
        
        return good_pair_count


# n : the length of input nums

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost nested loops, which is of O( n^2 )

## Space Compexity: O( 1 )
#
# The overhead in space is the stroage for loop index and counter, which are of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().numIdenticalPairs(nums = [1,2,3,1,1,3])
        self.assertEqual(result, 4)


    def test_case_2( self ):
    
        result = Solution().numIdenticalPairs(nums = [1,1,1,1])
        self.assertEqual(result, 6)    


    def test_case_3( self ):
        
        result = Solution().numIdenticalPairs(nums = [1,2,3])
        self.assertEqual(result, 0)                    



if __name__ == '__main__':

    unittest.main()        