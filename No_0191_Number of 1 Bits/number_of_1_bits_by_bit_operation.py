'''

Description

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
 

Follow up:

If this function is called many times, how would you optimize it?

'''



class Solution:
    def hammingWeight(self, n: int) -> int:
        
        num_of_1s = 0
        
        for i in range(64):
            
            num_of_1s += (n & 1)
            
            n = n >> 1
            
        return num_of_1s
            



# n : the input value of n

## Time Complexity: O( 1 )
#
# The overhead in time is the for lopp iterating on i, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage fot bit operation, which is of O( 1 ).



def test_bench():

    test_data = [2, 9, 63, 127, 1023]

    # expected output:

    '''
    1
    2
    6
    7
    10
    '''


    for n in test_data:

        print( Solution().hammingWeight(n) )

    return 



if __name__ == '__main__':

    test_bench()