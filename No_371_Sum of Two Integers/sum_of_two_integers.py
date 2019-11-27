'''

Description:

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        
        
        if b == 0:
        # base case:   
            
            return a
        
        else:
        # general case:

            # max of 32 bit integer
            MAX = 0x7FFF_FFFF

            # min of 32 bit integer
            MIN = 0x8000_0000

            # bitmask of 32 bit integer
            Mask = 0xFFFF_FFFF

            while b != 0:
                sum = a ^ b
                carry = a & b
                a, b = (sum)&Mask, (carry << 1) & Mask

            # if a is positive, direct return if a <= Max

            # if a is negative, get a's 32 bits complement positive first
            # then get 32-bit positive's Python complement negative
            return a if a <= MAX else ~(a ^ Mask)

# N : the bits needed for binary presenation of input b
#
## Time Complexity : O( N )
# the main task is the while loop
# each itertaion takes O(1) to carry out binary operation
# In summary, while loops has N iteration at most
# Thus, the time complexity is O( N )

## Space Complexity : O( 1 )
# It takes O( 1 ) to create some variables to store the result of binary operation

        
if __name__ == "__main__":
    
    test_bench = Solution()
    print( test_bench.getSum(1, 2) )

    print( test_bench.getSum(-2, 3) )

    print( test_bench.getSum(-3, -5) )
    
    