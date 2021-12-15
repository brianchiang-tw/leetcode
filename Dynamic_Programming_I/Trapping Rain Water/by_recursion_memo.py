from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        def water_dam(left, right, l_wall, r_wall):
            
            if left >= right:
                # Stop update water volume when index crossing
                return 0
            
            
            l_wall = max(l_wall, height[left])
            r_wall = max(r_wall, height[right])
            
            
            ## volume is decided by min(l_wall, r_wall)
            if l_wall <= r_wall:
                return l_wall - height[left] + water_dam(left+1, right, l_wall, r_wall)
            
            else:
                return r_wall - height[right] + water_dam(left, right-1, l_wall, r_wall)
            
        # -----------------------------------------------------------------------------
        n = len(height)
        return water_dam( 0, n-1, height[0], height[n-1])


import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().trap( height=[0,1,0,2,1,0,1,3,2,1,2,1] )
        self.assertEqual(result, 6)


    def test_case_2(self):

        result = Solution().trap( height=[4,2,0,3,2,5] )
        self.assertEqual(result, 9)


if __name__ == '__main__':

    unittest.main()