from typing import List

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        array_sum = 0
        
        local_min_sum, global_min_sum = 0, float('inf')
        local_max_sum, global_max_sum = 0, float('-inf')
        
        for number in A:
            
            local_min_sum = min( local_min_sum + number, number )
            global_min_sum = min( global_min_sum, local_min_sum )
            
            local_max_sum = max( local_max_sum + number, number )
            global_max_sum = max( global_max_sum, local_max_sum )
            
            array_sum += number
        
        
        
        # global_max_sum denotes the maximum subarray sum without crossing boundary
        # arry_sum - global_min_sum denotes the maximum subarray sum with crossing boundary
        
        if global_max_sum > 0:
            return max( array_sum - global_min_sum, global_max_sum )
        else:
            # corner case handle for all number are negative
            return global_max_sum



import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().maxSubarraySumCircular( [1,-2,3,-2] )
        self.assertEqual(result, 3)


    def test_case_2(self):

        result = Solution().maxSubarraySumCircular( [5,-3,5] )
        self.assertEqual(result, 10)

    def test_case_3(self):

        result = Solution().maxSubarraySumCircular( [-3,-2,-3] )
        self.assertEqual(result, -2)


if __name__ == '__main__':

    unittest.main()