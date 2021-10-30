from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        # --------------------------------------------------------------
        def backtrack(cur_index, leftmost_idx):
            
            # base case
            if leftmost_idx == start:
            
                # start index can jump to destination index
                return True
            
            
            # base case
            if cur_index < start:
                
                # start index cannot jump to destination index
                return False
            
            
            # general cases:
            if cur_index + nums[cur_index] >= leftmost_idx:
                # update leftmost index we can reach so far
                leftmost_idx = cur_index
            
            return backtrack(cur_index-1, leftmost_idx)
            
        
        # --------------------------------------------------------------
        size = len(nums)
        start, destination = 0, size-1
        return backtrack(cur_index=destination-1, leftmost_idx=destination)





import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().canJump( nums=[2,3,1,1,4] )
        self.assertEqual(result, True)
        return
    
    def test_case_2(self):

        result = Solution().canJump( nums=[3,2,1,0,4] )
        self.assertEqual(result, False)
        return


if __name__ == '__main__':

    unittest.main()