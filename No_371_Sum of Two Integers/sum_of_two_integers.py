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
        # stop condition:   
            
            return a
        
        else:
        # inductive step:
        
            # digit sum
            sum = a ^ b
            
            # carry bit will propagate to higer bit by left shift
            carry = a & b
            
            return sum + (carry << 1 )
        

        
if __name__ == "__main__":
    
    test_bench = Solution()
    print( test_bench.getSum(1, 2) )

    print( test_bench.getSum(-2, 3) )
    
    