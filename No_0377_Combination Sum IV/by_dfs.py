'''

Description:

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.



Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

'''

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
    
        # look-up table
        combination_count = {}
        
        # --------------------------------
        
        def dfs(wanted):
            
            ## base cases:
            
            if wanted < 0:
                # stop condition for negative number
                return 0
            
            elif wanted == 0:
                # stop condition for perfect match
                return 1
            
            if wanted in combination_count:
                # quick resposne by look-up table
                return combination_count[wanted]
            
            ## general cases
            count = 0
            
            for number in nums:
                
                next_wanted = wanted - number

                count += dfs(next_wanted)
            
            combination_count[wanted] = count
            return count
        
        # --------------------------------
        
        return dfs(wanted=target)


# n : the length of nums
# T : the value of t

## Time Complexity: O( n T )
#
# The overhead in time is the cost of recursion depth, which is of O( n T )

## Space Complexity: O( T )
#
# The ovehead in space is the storage for recursion stack, which is of O( T )


import unittest

class Testing( unittest.TestCase ):

    def setUp(self) -> None:
        self.solver = Solution().combinationSum4
        return

    def test_case_1( self ):

        result = self.solver(nums=[1,2,3], target=4)
        self.assertEqual(result, 7)

    def test_case_2( self ):

        result = self.solver(nums=[9], target=3)
        self.assertEqual(result, 0)


if __name__ == '__main__':

    unittest.main()