'''

Description:

A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

 

Example 1:

Input: N = 1, A = 2, B = 3
Output: 2
Example 2:

Input: N = 4, A = 2, B = 3
Output: 6
Example 3:

Input: N = 5, A = 2, B = 4
Output: 10
Example 4:

Input: N = 3, A = 6, B = 4
Output: 8
 

Note:

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000

'''


class Solution:
    
    def gcd(self, a, b):

        while b:
            a, b = b, a%b

        return a


    def nthMagicalNumber(self, n, a, b):
        


        lower_bound, upper_bound, lcm = 1, max(a,b)*n, (a * b) // self.gcd(a, b)

        while lower_bound <= upper_bound:           
            mid = lower_bound + (upper_bound - lower_bound)//2    

            total_count_of_multiplier = mid//a + mid//b - mid//lcm

            if total_count_of_multiplier == n: 
                break

            if total_count_of_multiplier < n: 
                lower_bound, upper_bound = mid+1, upper_bound

            else:
                lower_bound, upper_bound = lower_bound, mid-1
                

        while mid%a and mid%b:
            mid -= 1

        return mid % 1000000007


# N: max(a, b)
# k: the k-th order magical number 

## Time complexity: O( kN )
#
# This procedure is a variant binary search, the upper bound is set by max(a, b) * k = O( kN )

## Space complexity: O( 1 )
#
# The overhead of space is the variable for arithmetic operation of constant size.

def test_bench():

    test_data = [
                    (1, 2, 3),
                    (4, 2, 3),
                    (5, 2, 4),
                    (3, 6, 4)
                ]


    # expected output:
    '''
    2
    6
    10
    8
    '''


    for test in test_data:

        n_th_magical_number = Solution().nthMagicalNumber( n = test[0], a = test[1], b = test[2] )

        print( n_th_magical_number )

    return



if __name__ == '__main__':

    test_bench()