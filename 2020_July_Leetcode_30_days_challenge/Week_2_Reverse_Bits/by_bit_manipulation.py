'''

Description:

Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.



Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Follow up:

If this function is called many times, how would you optimize it?

'''



class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0
        
        for i in range(32):
            
            result = (result << 1) | (n & 1)
            
            n >>= 1
        
        return result


## Time Complexity: O( 32 )= O( 1 )
#
# The overhead in time is the cost of for loop, which is of O( 32 ) = O( 1 ).

## Space Complexity: O( 1 ) 
#
# The overhead in space is the storage for temporary variable and loop index, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().reverseBits( n = int('00000010100101000001111010011100', base = 2))
        self.assertEqual( result, 964176192)


    def test_case_2( self ):
    
        result = Solution().reverseBits( n = int('11111111111111111111111111111101', base = 2))
        self.assertEqual( result, 3221225471)


if __name__ == '__main__':

    unittest.main()