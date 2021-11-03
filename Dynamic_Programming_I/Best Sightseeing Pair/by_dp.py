from typing import List

class Solution():

    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        # best neighbor with distance degrading factor, as value[i] + (i - j)
        max_local_neighbor = 0

        # best sightseeing pair, as value[i] + (i - j) + value[j]
        best_pair = 0

        # scan each possible value, as value[j]
        for cur_value in values:

            # update best sightseeing pair up to current position
            best_pair = max(best_pair, max_local_neighbor + cur_value)

            # update max local neighbor, as value[j]
            # -1 on each iteration is the distnace degrading factor to express (i-j) tern, definedby description
            max_local_neighbor = max(max_local_neighbor, cur_value) - 1

        return best_pair


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