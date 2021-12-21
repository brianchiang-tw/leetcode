from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        global_pos = 0
        
        
        def dp( i ):
            
            ## Parameter
            # input i: ending index of array i
            # output : length of positive product subarray, length of negative product subarray
            
            ## Base case:
            if i == 0:
                
                if nums[0] > 0:
                    
                    return 1, 0, 1
                
                elif nums[0] < 0:
                    return 0, 1, 0
                
                else:
                    return 0, 0, 0
            
            
            ## General cases
            
            prev_pos, prev_neg, max_pos_length = dp(i-1)
            cur_pos, cur_neg = 0, 0
            
            if nums[i] > 0:
                
                # positive = previous positive * positive number
                cur_pos = prev_pos + 1
                
                if prev_neg:
                    # negative = previous negative * positive number
                    cur_neg = prev_neg + 1
                    
            elif nums[i] < 0 :
                
                # negative = previous positive * negative number
                cur_neg = prev_pos + 1
                
                if prev_neg:
                    # positive = previous negative * negative number
                    cur_pos = prev_neg + 1
            
            
            max_pos_length = max(max_pos_length, cur_pos )
            return cur_pos, cur_neg, max_pos_length
        
        # ----------------------------------------
        
        # third return value is maximum length of subarray with positive product
        return dp( len(nums)-1 )[2]
                

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().getMaxLen([1,-2,-3,4])
        self.assertEqual(result, 4)


    def test_case_2( self ):

        result = Solution().getMaxLen([0,1,-2,-3,-4])
        self.assertEqual(result, 3)


if __name__ == '__main__':

    unittest.main()
