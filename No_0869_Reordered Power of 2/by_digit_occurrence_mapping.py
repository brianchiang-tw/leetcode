'''

Description:

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

 

Example 1:

Input: 1
Output: true



Example 2:

Input: 10
Output: false



Example 3:

Input: 16
Output: true



Example 4:

Input: 24
Output: false



Example 5:

Input: 46
Output: true
 

Note:

1 <= N <= 10^9

'''



class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        def make_signature(n: int):
            
			## base case
            if n == 0:
                return 0
            
			
			## general case
			
            leading, remaining = divmod(n, 10)
            return make_signature(leading) + ( 10 ** remaining )
        
        # ---------------------------------------------------------
        
        signature_of_N = make_signature(N)
        
		# check each possible power of 2
        for i in range(32):
            
			# get power of 2 by bitwise operation, and check signature
            if make_signature( 1 << i ) == signature_of_N:
			
				# Accept if at least one power of 2's signature is the same with N's signature
                return True
        
		# Reject otherwise
        return False


## N : the input value

## Time Complexity: O( log N )
#
# The overhead in time is the cost of recursion call stack, which is of O( log N )

## Space Complexity: O( log N )
# 
# The overhead in space is the storage for recrsion call stack, which is of O( log N )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().reorderedPowerOf2( N = 1 )
        self.assertEqual(result, True)


    
    def test_case_2( self ): 

        result = Solution().reorderedPowerOf2( N = 10 )
        self.assertEqual(result, False)



    def test_case_3( self ):

        result = Solution().reorderedPowerOf2( N = 16 )
        self.assertEqual(result, True)


    
    def test_case_4( self ): 

        result = Solution().reorderedPowerOf2( N = 24 )
        self.assertEqual(result, False)



    def test_case_5( self ): 

        result = Solution().reorderedPowerOf2( N = 46 )
        self.assertEqual(result, True)

if __name__ == '__main__':

    unittest.main()        

