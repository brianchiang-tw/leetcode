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
            # base case:
            return float(1)
        
        elif n == 1:
            # base case:
            return float(x)
        
        elif n < 0:
            
            # x ^ negative exponent = 1 / x ^ positive exponent
            return 1 / self.myPow( x, -n )
        
        else:
            # general case:
            
            if n % 2 == 0:
                half = self.myPow( x, n / 2)
                return half*half
            
            else:
                half = self.myPow( x, (n-1)/2 )
                return half * half * x
        

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