from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        
        # key: index pair of covered range
        # value: maximized value of picking
        memo = {}
        
        # --------------------------------------------
        
        def helper(left, right):
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            if left > right:
                return 0
            
            elif left == right:
                return nums[left]
            
            take_i = helper(left, right-2) + nums[right]
            not_to_take_i = helper(left, right-1) + 0
            
            optimal = max(take_i, not_to_take_i)
            memo[(left, right)] = optimal
            return optimal
        
        # --------------------------------------------
        size = len(nums)
        
        # Handler for corner cases
        if size == 0:
            return 0
        
        elif size == 1:
            return nums[0]
        
        elif size == 2:
            return max(nums[0], nums[1])
			
        # Optimal maximized profit = max( Consider Head but Tail is excluded, or Consider Tail but Head is excluded )
        return max( helper(0, size-2), helper(1, size-1))



import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().rob( nums=[2, 3, 2] )
        self.assertEqual(result, 3)
        return


    def test_case_2(self):

        result = Solution().rob( nums=[1, 2, 3, 1] )
        self.assertEqual(result, 4)
        return    


if __name__ == '__main__':

    unittest.main()