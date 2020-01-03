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

'''


class Solution:
    def reverseBits(self, n: int) -> int:
        
        rev_bits = 0
        for i in range( 32 ):
            
            rev_bits = rev_bits << 1
            
            # rev_bits get binary bit from LSB to MSB of n
            rev_bits = rev_bits | ( n & 1 )
            
            n = n >> 1
            
        
        return rev_bits
        



# n : the number of input n 

## Time Complexity: O( 1 )
#
# The major overhead in time is for loop iterating on i, which is of O( 32 ) = O( 1 )


## Spae Complexity: O( 1 )
#
# The overhead in space is the storage for output integer, of fixed 32 bit lemgth, which is of O( 1 ).



def test_bench():

    test_data = [43261596, 4294967293]

    # expected output:
    '''
    964176192
    3221225471
    '''


    for n in test_data:

        print( Solution().reverseBits(n) )

    return 



if __name__ == '__main__':

    test_bench()
        
        