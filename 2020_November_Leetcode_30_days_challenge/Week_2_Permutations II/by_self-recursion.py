'''

Description:

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


 
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

'''


from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        def helper():
            size = len(nums)

            if size == 0:
                # base case:
                return [ [] ]
            
            elif size == 1:
                # base case:
                return [ nums ]

            
            # general case:

            result = []
            prev_num = None

            for idx in range(size):

                if nums[idx] == prev_num:
                    # skip permutation with repeated elements
                    continue

                prev_num = nums[idx]
				
				# nums[idx] as head, concatenate with other permutations on remaining numbers
                for permu in self.permuteUnique( nums[:idx] + nums[idx+1:] ):
                    result.append( [ nums[idx] ] + permu )

            return result
        # -----------------------------------------------------------------------
        nums.sort()
        return helper()


# n : the length of nums

## Time Complexity: O( n! )
#
# The overhead in time is the cost of permutation generation, which is of O( n! )

## Space Complexity: O( n! )
#
# The overhead in space is the stroage for all permuation, which is of O( n! )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().permuteUnique( nums=[1,1,2] )
        self.assertCountEqual(result, [[1,1,2],[1,2,1],[2,1,1]] )


    def test_case_2( self ):

        result = Solution().permuteUnique( nums=[1,2,3] )
        self.assertCountEqual(result, [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] )


if __name__ == '__main__':

    unittest.main()        