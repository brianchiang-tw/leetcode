from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        # record of left max wall
        l_wall = [ 0 for _ in range(n) ]
        
        # record of right max wall
        r_wall = [ 0 for _ in range(n) ]
        
        l_wall[0] = height[0]
        r_wall[-1] = height[-1]
        
        # update max wall in DP
        for i in range(1, n ):
            l_wall[i] = max(l_wall[i-1], height[i])
            r_wall[-i-1] = max(r_wall[-i], height[-i-1])

        
        water = 0
        
        # collec water in DP
        for i in range( 1, n-1 ):
            
            ## volume is decided by min(l_wall, r_wall)
            effective_wall = min(l_wall[i], r_wall[i])
            
            water += effective_wall - height[i]
            
        return water


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