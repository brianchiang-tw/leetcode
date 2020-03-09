'''

Description:

Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.

 

Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984
 

Constraints:

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
It's guaranteed that the result will be in range [1, 2 * 10^9]

'''



from math import gcd

class Solution:
    

    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        
        def lcm( x, y):
            
            # From number theory,
            # gcd(x,y) * lcm(x,y) = x * y
            
            return  x * y  // gcd(x,y)        
        
        # -----------------------------------
        
        def total_num_of_multiples( number, a, b, c):
            
            # From set theory,
            # count the total number of mutiples of a, b, c, range from 1 to number.
            ab = lcm(a,b)
            bc = lcm(b,c)
            ac = lcm(a,c)

            abc = lcm(a, bc)

            result = number // a + number // b + number // c 
            result -= number // ab + number // bc + number // ac
            result += number // abc

            return result        
        
        # -----------------------------------
        
        # Goal:
        # Find the smallest number k, such that k has n multiples of a, b, or c.
        
        # Binary search approach
        lower = 1
        upper = 2 * (10 ** 9)
        
        while lower < upper:
            
            mid = lower + (upper - lower) // 2
            
            count_of_u_number = total_num_of_multiples(mid, a, b, c)

            if count_of_u_number >= n:
                upper = mid
                
            else:
                lower = mid+1
            
        return lower



# n : the maximum of input parameters

## Time Complexity: O( ( log n )^2 )
#
# The overhead in time is the cost of binary search, of O( log n), combined with gcd and lcm, of O( log n ).
# It takes O( ( log n)^2 ) in total.

## Space Complexity: O(1)
#
# The overhead in space is the storage for looping viaralbe, and mathematical computation, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'n a b c')
def test_bench():

    test_data = [
                    TestEntry( n = 3, a = 2, b = 3, c = 5),
                    TestEntry( n = 4, a = 2, b = 3, c = 4),
                    TestEntry( n = 5, a = 2, b = 11, c = 13),
                    TestEntry( n = 1000000000, a = 2, b = 217983653, c = 336916467),
                ]

    # expected output:
    '''
    4
    6
    10
    1999999984
    '''

    for t in test_data:
        print( Solution().nthUglyNumber( *t ) )

    return



if __name__ == '__main__':

    test_bench()