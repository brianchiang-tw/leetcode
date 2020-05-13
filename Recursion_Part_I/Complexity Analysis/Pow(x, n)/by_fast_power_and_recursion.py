'''

Description:

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000



Example 2:

Input: 2.10000, 3
Output: 9.26100



Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

'''



class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            # Base case:
            return 1
        
        elif n == 1:
            # Base case:
            return x
        
        elif n < 0:
            # General case:
            # x ^ (-n) = (1/x) ^ n
            return  self.myPow( 1/x, -n)
        
        
        # Recurrence of fast power
        
        if n & 1:
            return x * self.myPow( x*x, n // 2)
        else:
            return self.myPow( x*x, n // 2)



# n : the order of exponent

## Time Compexity: O( log n )
#
# The overhead in time is the cost of recursion execution tree, which is of O( log n )

## Space Complexity: O( log n )
#
# The overhead in space is the storage for recursion call stack, which is of O( log n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'x n')

def test_bench():

    test_data = [
                    TestEntry( x = 2, n = 1 ),
                    TestEntry( x = 2, n = 10 ),
                    TestEntry( x = 2, n = -2 ),
                    TestEntry( x = 2, n = 0 ),
                    TestEntry( x = 2.1, n = 3 ),
                ]

    # expected output:
    '''
    2
    1024
    0.25
    1
    9.261000000000001
    '''

    for t in test_data:

        print( Solution().myPow(x = t.x, n = t.n) )

    return



if __name__ == '__main__':

    test_bench()    