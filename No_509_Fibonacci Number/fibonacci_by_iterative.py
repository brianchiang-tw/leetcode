'''

Description:

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.

'''


class Solution:
    def fib(self, N: int) -> int:
        
        # Base case:
        a, b = 0, 1
        
        if N <= 1:
            return N
        
        # General case:
        for i in range(2, N+1):
            
            a, b = b, a+b
            
        return b



# n : the value of input N

## Time Complexity: O( n )
#
# The major overhead in time is the for loop iterating over i, which is of O( n )


## Space Complexity: O( 1 )
#
# The major overhead in space is to maintain a, b for general case computation, which is of O( 1 )




def test_bench():

    test_data = [0, 1, 2, 3, 4, 5, 10, 30]

    # expected output:
    '''
    0
    1
    1
    2
    3
    5
    55
    832040
    '''



    for n in test_data:

        print( Solution().fib(n) )
    
    return 



if __name__ == '__main__':

    test_bench()