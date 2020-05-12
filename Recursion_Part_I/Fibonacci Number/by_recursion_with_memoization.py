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
    
    def __init__(self):
        
        self.cache = {}
    
    def fib(self, N: int) -> int:
        
        if N in self.cache:
            return self.cache[N]
        
        if N <= 1:
            return N
        
        else:
            result = self.fib(N-1) + self.fib(N-2)
            
            # update cache data
            self.cache[N] = result
            
            return result



# n : the number of input value N 

## Time Comeplxity: O( n )
#
# The overhead in time is the cost of recursion depth, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for cache, which is of O( n ).



def test_bench():

    test_data = [
                    0,1,2,3,4,5,29,30
                ]            


    # expected output:
    '''
    0
    1
    1
    2
    3
    5
    514229
    832040
    '''

    for t in test_data:

        print( Solution().fib( N = t ) )

    return



if __name__ == '__main__':

    test_bench()    