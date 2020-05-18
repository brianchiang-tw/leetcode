'''

Description:

Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.

 

Example 1:

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]
Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
Example 4:

Input: n = 1
Output: []
 

Constraints:

1 <= n <= 100

'''


from typing import List
from math import gcd

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        simple_fraction = []
        
        for denominator in range(2, n+1):
            
            denom_is_even = True if denominator % 2 == 0 else False
            
            for numerator in range(1, denominator):
                
                if denom_is_even and numerator % 2 == 0:
                    # even numbers must have gcd = 2, therefore no chance to make simplified fraction
                    continue
                
                if gcd(numerator, denominator) == 1:
                    
                    simple_fraction.append( f"{numerator}/{denominator}")
                    
        return simple_fraction


# n : the input value of n

## Time Complexity: O( n^2 log n )
#
# The overhead in time is the cost of nested loops of O( n^2 ), plus the cost of gcd of O( log n )
# It takes O( n^2 log n ) in total.

## Space Complexity: O( n^2 )
#
# The overhead in space is the cost for ouput, simple_fraction, which is of O( n^2 ).


def test_bench():

    # expected output is in the comment
    test_data = [
                    1,  # []
                    2,  # ['1/2']
                    3,  # ['1/2', '1/3', '2/3']
                    4,  # ['1/2', '1/3', '2/3', '1/4', '3/4']
                    5,  # ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5']
                    6,  # ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6']
                    7,  # ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6', '1/7', '2/7', '3/7', '4/7', '5/7', '6/7']
                    8,  # ['1/2', '1/3', '2/3', '1/4', '3/4', '1/5', '2/5', '3/5', '4/5', '1/6', '5/6', '1/7', '2/7', '3/7', '4/7', '5/7', '6/7', '1/8', '3/8', '5/8', '7/8']
                ]

    for test_n in test_data:

        print( Solution().simplifiedFractions( n = test_n ) )

    return



if __name__ == '__main__':

    test_bench()