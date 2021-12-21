from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        
        def dp( i ):
            
            if i == 0:
                
                ## Base case:
                # best pair = 0
                # max local neighbor with distance degrading factor = values[0]
                return 0, values[0]-1
            
            ## General cases
            prev_pair, prev_max_neighbor = dp(i-1)
            
            best_pair = max(prev_pair, values[i] + prev_max_neighbor)
            
            # -1 is distance degrading factor
            max_neighbor = max(prev_max_neighbor, values[i]) - 1
            
            return best_pair, max_neighbor
        
        # --------------------------------------------------
        return dp( len(values)-1 )[0]


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().maxScoreSightseeingPair( [8,1,5,2,6] )
        self.assertEqual(result, 11)


    def test_case_2( self ):

        result = Solution().maxScoreSightseeingPair( [1,2] )
        self.assertEqual(result, 2)


if __name__ == '__main__':

    unittest.main()