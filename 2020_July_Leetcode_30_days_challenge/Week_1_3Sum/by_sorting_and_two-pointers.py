'''

Description:

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''



from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        size = len(nums)
        solution = []
        
        for idx in range(0, size-2):
            
			# avoid repetition
            if idx and nums[idx] == nums[idx-1]:
                idx +=1
                pass
                continue
                
            first_num = nums[idx]
            
            target = -first_num
            
            i, j = idx+1, size-1
            
            
            while i < j:
                
                cur_two_sum = nums[i] + nums[j]
                
                if cur_two_sum > target:
                    j -=1
                elif cur_two_sum < target:
                    i += 1
                else:
                    solution.append( [ first_num, nums[i], nums[j] ] )
                    i += 1
                    j -= 1
                    
					# avoid repetition
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    
					# avoid repetition
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                    
        return solution



# n : the length of nums

## Time Complexity: O( n^2 )
#
# The overhead in time is the cost of nested loop, which is of O( n ^ 2)

## Space Complexity: O( n )
#
# The overhead in space is the storage for output solution, which is of O( n )

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().threeSum( nums = [-1, 0, 1, 2, -1, -4] )
        self.assertEqual(result, [[-1, -1, 2], [-1, 0, 1]])



if __name__ == '__main__':

    unittest.main()