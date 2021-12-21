from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def dp( i ):
            
            ## Base case:
            if i == 0:
                # coverage, last_jump index, count of jump
                return nums[0], nums[0], 1
            
            ## General cases
            prev_coverage, prev_jump_idx, prev_jumps = dp(i-1)
            
            cur_coverage = max(prev_coverage, i + nums[i] )
            cur_jump_idx = prev_jump_idx
            jumps = prev_jumps
            
            if i == prev_jump_idx:
                cur_jump_idx = cur_coverage
                jumps += 1
                
            return cur_coverage, cur_jump_idx, jumps
        
        # -------------------------------------------------
        if len(nums) == 1:
            # Quick response on corner case when array size = 1
            return 0
        
        # third return value is the counter of jumps
        last_station = len(nums)-1
        return dp( last_station-1 )[2]
        


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