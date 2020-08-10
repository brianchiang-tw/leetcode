'''

Description:

Given two positive integers n and k, the binary string  Sn is formed as follows:

S1 = "0"
Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001". The first bit is "0".



Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001". The 11th bit is "1".



Example 3:

Input: n = 1, k = 1
Output: "0"



Example 4:

Input: n = 2, k = 3
Output: "1"
 

Constraints:

1 <= n <= 20
1 <= k <= 2n - 1

'''



class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        binstr_length = [0] * (n+1)
        
        binstr_length[1] = 1
        
        for i in range(2, n+1):
            binstr_length[i] = 2 * binstr_length[i-1] + 1
            
        # ---------------------------------------------------
        def find_bit(n, k):
            
            if n == 1:
                # base case:
                return 0
            
            else:
                # general case:
                
                if k  <= binstr_length[n-1]:
                    
                    # k is on the left half, S_n-1
                    
                    return find_bit(n-1, k)
                
                elif k == (binstr_length[n-1] + 1):
                    
                    # k is on middle point, "1"
                    
                    return 1
                
                else:
                    toggle = lambda bit: bit^1
                    
                    # k is on the right half, reverse( invert(S_n-1) )
                    
                    return toggle( find_bit(n - 1, 2 * (binstr_length[n-1] + 1) - k) )
                
        # ---------------------------------------------------
        return str( find_bit(n, k) )



# n : the value of input n

## Time Complexity: O( n )
#
# The overhead in time is the cost of binary string generation, which is of O( n )

## Space Compleixty: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )



import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().findKthBit(n=3, k=1)
        self.assertEqual(result, '0')


    def test_case_2( self ):
        
        result = Solution().findKthBit(n=4, k=11)
        self.assertEqual(result, '1')


    def test_case_3( self ):
        
        result = Solution().findKthBit(n=1, k=1)
        self.assertEqual(result, '0')


    def test_case_4( self ):
    
        result = Solution().findKthBit(n=2, k=3)
        self.assertEqual(result, '1')



if __name__ == '__main__':

    unittest.main()