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
        

# n : the number of exponent

## Time Complexity: O( log n )
#
# The major overhead in time is the function call depth of divide-and-conquer based on 2, which is of O( log n)

## Space Complexity: O( log n)
#
# The major overhead in space is to maintain call stack for myPow, whoose call depth is O( log n)



def test_bench():

    test_data = [
                    ( 2, 0),
                    ( 2, 1),
                    ( 2, -1),
                    ( 2, 10),
                    ( 2, -10),
                    ( 2, 11),
                    ( 2, -11)
                ]

    # expected output:
    '''
    1.0
    2.0
    0.5
    1024.0
    0.0009765625
    2048.0
    0.00048828125
    '''


    for base, exp in test_data:

        print( Solution().myPow( x = base, n = exp) )

    return



if __name__ == '__main__':
    
    test_bench() 