'''

Description:

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

'''


from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        duplicates = []
        
        # For number k, its home index is (k-1)
        
        for idx, cur_num in enumerate(nums):
            
            home_idx = abs(cur_num)-1
            
            if nums[home_idx] < 0:
                
                # nums[home_idx] has been visited before
                # (home_idx + 1) is repeated twice
                duplicates.append( home_idx + 1 )
				
            else:
                
                # Use negative sign to mark that nums[home_idx] as visited
                nums[home_idx] = -nums[home_idx]
                    
        return duplicates



# n : the length of input list, nums

## Time Complexity: O(n)
#
# The overhead in time is the cost of loop iteration, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, duplicates, which is of O( n ).

import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().findDuplicates( nums=[4,3,2,7,8,2,3,1] )
        self.assertEqual(result, [2, 3] )


if __name__ == '__main__':

    unittest.main()