'''

Description:

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False

'''



'''
Sum of two squares theorem:
An integer greater than one can be written as a sum of two squares if and only if its prime decomposition contains no prime congruent to 3 modulo}4 raised to an odd power.
'''

from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        # general form:
        # a^2 + b^2 == c where a <= b
        
        # c = (p1^q1) * (p2^q2) ... * (pk^qk)
        
        
        factor = 2
        
        # scan each prime factor
        while factor * factor <= c:
            
            exponent_of_factor = 0
            
            # check whether " facotr | c " or not
            if c % factor == 0:
                
                # get the exponent of current factor
                while c % factor == 0:
                    
                    # accumulate the exponenet of prime factor
                    exponent_of_factor += 1
                    
                    # update c
                    c = c // factor
                
                
                # Reject factor decomposition in the form: " (4k+3)^q | c ", where q is odd integer
                if factor % 4 == 3 and exponent_of_factor % 2 != 0:
                    return False
            
            # try next factor
            factor += 1
        
        # Reject number in the form: c = 4k+3 where k is non-negative integer
        return c % 4 != 3



# n : the input value

## Time Complexity: O( sqrt( n ) * log(n) )
#
# The overhead in time is the outer loop iterating on a <= b, which is of O( sqrt(n) ).
# And the innter while loop iterating on c % factor == 0, which is of O( log(n) )

## Space Complexity: O( 1 )
#
#

## Space Complexity: O( 1 )
#
# The overhead in space is the looping index and factpr, exponent_of_factor for computation, which is of O( 1 ).




def test_bench():

    test_data = [3, 5, 13, 25, 18, 28, 33]

    # expected output:
    '''
    False
    True
    True
    True
    True
    False
    False    
    '''

    for number in test_data:

        print( Solution().judgeSquareSum(number) )
    
    return 



if __name__ == '__main__':

    test_bench()