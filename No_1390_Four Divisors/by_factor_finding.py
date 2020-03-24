'''

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
 

Constraints:

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5

'''


from typing import List
from math import sqrt

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        sum_of_factor = 0
        
        for x in nums:
            
            factors = set()
            
            # collection all factors into set
            for i in range(1, int(sqrt(x)+1) ):
                
                if x % i == 0:
                    
                    factors.add( i )
                    factors.add( x // i )
                    
                    if len( factors ) > 4:
                        # early breaking when there is too many factors
                        break
                        
                
            if len( factors ) == 4:
                # update sum of four divisors
                sum_of_factor += sum(factors)
        
        return sum_of_factor



## Time Complexity: O( sqrt(n) )
#
# The overhead in time is the cost of outerloop, which is of O( sqrt(n) )

## Space Complexity: O( sqrt(n) )
#
# The overhead in space is the storage for set, factors, which is of O( sqrt(n) )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'numbers')
def test_bench():

    test_data = [
                    TestEntry( numbers = [21,4,7] )
                ]        

    for t in test_data:

        print( Solution().sumFourDivisors( t.numbers) )

    return



if __name__ == '__main__':

    test_bench()