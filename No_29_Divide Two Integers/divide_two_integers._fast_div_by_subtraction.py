class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        negative = False
        
        if ( dividend < 0 ) != ( divisor < 0 ):
            # determine the sign of quotient
            negative = True
            
        # mapping to positive number division
        
        divisor, dividend = abs(divisor), abs(dividend)
        
        total_quotient = 0
        test_sum = divisor
        
        # keep carrying out divison if dividend > divisor
        while test_sum <= dividend:
            
            current_quotient = 1
            
            # enlarge twice by divisor and test the_sum
            while( test_sum + test_sum ) <= dividend :
                test_sum += test_sum
                current_quotient += current_quotient
            
            # get the remainder of division after testing
            dividend -= test_sum
            
            # reset test_sum to divisor for next round division
            test_sum = divisor
            
            # accumulate quotient of current division
            total_quotient += current_quotient
        
        # handling the sign of quotient and lowerbound
        total_quotuent = max( -total_quotient if negative else total_quotient, -2147483648 )
        
        # handling upperbound
        total_quotient = min( total_quotuent, 2147483647 )
        
        return total_quotient


# N : the value of dividend
# M : the value of divisor
                
## Time Complexity

# O( log(N/M) )
# the core of the function, divide, is the enlarge and check while loop on test_sum
# this loop takes O( log(N/M) ) steps to reach the nearest divided integer value

## Space Complexity
# O(1)
# the function, divide, need extra O(1) space for mathematical operation variables,
# such as negative, total_quotient, current_quotient, as well as test_sum



def test_bench():

    pair_for_test_division = [ (10, 3), (7, -3) ]

    for pair in pair_for_test_division:

        quotient = Solution().divide( dividend = pair[0], divisor = pair[1] )

        print( quotient )

        # expected output:
        '''
        3
        -2
        '''



if __name__ == '__main__':

    test_bench()

