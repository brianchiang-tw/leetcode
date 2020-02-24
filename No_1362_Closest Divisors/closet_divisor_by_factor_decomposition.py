'''

Description:

Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

 

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.



Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]
 

Constraints:

1 <= num <= 10^9

'''



from math import sqrt
from typing import List
class Solution:
    
    def factor_decompose(self, num: int)->List[int]:
        
        # Searach from the best balanced pair of factor pair
        
        for i in range( round(sqrt(num)), 0, -1):
            
            if num % i == 0:
                return [i, num//i]
    
    
    
    def closestDivisors(self, num: int) -> List[int]:
        
        # Decompose num+1 and num+2 respectively
        # Return the closet factor pair
        
        factor_pairs = list(map( self.factor_decompose, [ num+1, num+2 ] ))
        
        func = lambda pair: abs(pair[0]-pair[1])

        first_diff, second_diff = map( func, factor_pairs)
        
        if first_diff < second_diff:
            return factor_pairs[0]
        else:
            return factor_pairs[1]



# n : the value of input, num.

## Time Complexity: O( sqrt(n) )
#
# The overhead in time is the cost of function, factor_decompose*(), which is of O( sqrt(n) ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and temporary variable, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'num')
def test_bench():

    test_data = [
                    TestEntry( num = 8 ),
                    TestEntry( num = 123 ),
                    TestEntry( num = 999 ),
                    TestEntry( num = 1),
                    TestEntry( num = 10**9 ),
                ]

    # expected output:
    '''
    [3, 3]
    [5, 25]
    [25, 40]
    [1, 2]
    [23658, 42269]
    '''

    for t in test_data:
        print( Solution().closestDivisors( num = t.num) )
    
    return



if __name__ == '__main__':

    test_bench()

    