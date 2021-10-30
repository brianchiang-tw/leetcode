from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            
            # Quick response for empty input
            return 0
        
        
        # key: index pair, which means the range taken into consideration
        # value: maximized value
        memo =  { 
                (0,0): nums[0], 
                }
        
        # ----------------------------
        
        def helper(idx):
            
            if idx < 0:
				# base case:
                return 0
            
            if (0,idx) in memo:
				# base case:
                return memo[(0, idx)]
            
			
            # general case:
			
            take_i = helper(idx-2) + nums[idx]
            not_to_take_i = helper(idx-1) + 0
            
            optimal = max(take_i, not_to_take_i)
            memo[(0, idx)]= optimal
            
            return optimal
        
        # ----------------------------
        
        return helper( idx=len(nums)-1 )




import unittest

class Testing( unittest.TestCase):

    def test_case_1(self):

        result = Solution().rob( nums=[1,2,3,1])
        self.assertEqual(result, 4)
        return 

    
    def test_case_2(self):

        result = Solution().rob( nums=[2,7,9,3,1])
        self.assertEqual(result, 12)
        return 


if __name__ == '__main__':
    unittest.main()        