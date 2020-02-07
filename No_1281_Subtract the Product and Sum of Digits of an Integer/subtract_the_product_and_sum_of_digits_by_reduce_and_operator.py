'''

Description:

    Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5

'''



from functools import reduce
from operator import mul
from operator import add
class Solution:
    
    def product_subtract_sum(self, n):
        
        # convert number into a list of digits
        digit_list = list( map(int, str(n) ) )
        
        # compute product of digits
        product = reduce( mul, digit_list)
        
        # compute summation of digits
        summation = reduce( add, digit_list )
        
        # compute product minus summation
        return ( product - summation )
        
    
    
    
    def subtractProductAndSum(self, n: int) -> int:
        
        return self.product_subtract_sum( n )



# N : the value of input

## Time Complexity : O( log10 N ) = O( log N )
#
# It seems to be O( 1 ) at first glimpse, but actually it is O( log N )
# The overhead in time is the length of digit_list, which grows in O( log10 N )
# Hint: think of the decimal notation of a number

## Space Complexity : O( 1 )
#
# The overhead in space is to maintain a list a temp variable for produce, sum as well as subtraction.
# All of them are fixed size of O( 1 )



def test_bench():

    test_data = [234, 4421]

    # expected output:
    '''
    15
    21
    '''


    for n in test_data:

        print( Solution().product_subtract_sum(n) )

    return



if __name__ == '__main__':

    test_bench()
