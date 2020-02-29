'''

Description:

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.



Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.

'''



class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n <= 3:
            # n = 2 = 1 + 1, product = 1
            # n = 3 = 2 + 1, product = 2
            return n-1
        
        remain, product = n, 1
        
        while remain > 4:
            # Keep decompose with 3
            product *= 3
            remain -=3
            
        return product * remain



# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the while loop, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable and temporary variable for computation, which is of O( 1 ).

def test_bench():

    test_data = [2,3,4,5,6,7,8,9,10,50]


    # expected output:
    '''
    1
    2
    4
    6
    9
    12
    18
    27
    36
    86093442
    '''

    for n in test_data:

        print( Solution().integerBreak(n) )
    
    return 



if __name__ == '__main__':

    test_bench()