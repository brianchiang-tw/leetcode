'''

Description:

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true


Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

'''



class Solution:
    def isPowerOfFour(self, num):
        
        if num < 1: 
            return False
        
        elif num ==1 : 
            return True
        
        else:
            # Capture all (2^n)^k, by num & (num-1) == 0
            # Then screen out those numbers which are exact power of two only by 0xAAAAAAAA mask
            # Finally, we have number of (2^n)^k, where k >= 2
            return num & (num-1) == 0 and num & 0xAAAA_AAAA == 0



## Time Complexity: O( 1 )
#
# The overhead in time is the cost of bitwise operation, which is of O( 32) = O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):
        
        result = Solution().isPowerOfFour( num=16 )
        self.assertEqual(result, True)


    def test_case_2( self ):
        
        result = Solution().isPowerOfFour( num=5 )
        self.assertEqual(result, False)        


    def test_case_3( self ):
        
        result = Solution().isPowerOfFour( num=3 )
        self.assertEqual(result, False)        


    def test_case_3( self ):
        
        result = Solution().isPowerOfFour( num=256 )
        self.assertEqual(result, True)               


    def test_case_4( self ):
        
        result = Solution().isPowerOfFour( num=1 )
        self.assertEqual(result, True)                  


    def test_case_5( self ):
            
        result = Solution().isPowerOfFour( num=-4 )
        self.assertEqual(result, False)     



if __name__ == '__main__':

    unittest.main()