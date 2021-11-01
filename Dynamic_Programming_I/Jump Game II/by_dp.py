from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        size = len(nums)
        
        # destination is last index
        destination = size - 1
        
        dp = [0 for _ in range(size)]
        
        last_jump_index = 0
        
        # counter for jump
        jump = 0
        
        if size == 1:
            
            # Quick response if start index == destination index == 0
            return 0
        
        for i in range(0, size):
            
            # extend current coverage as further as possible
            dp[i] = max(dp[i-1], i + nums[i])
            
            if i == last_jump_index:
                # lazy jump
                last_jump_index = dp[i]
                
                jump += 1
                
                if dp[i] >= destination:
                    return jump
                
        return jump
        


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().jump( nums=[2,3,1,1,4])
        self.assertEqual(result, 2)
        return

    
    def test_case_2(self):


        result = Solution().jump( nums=[2,3,0,1,4])
        self.assertEqual(result, 2)
        return


if __name__ == '__main__':

    unittest.main()