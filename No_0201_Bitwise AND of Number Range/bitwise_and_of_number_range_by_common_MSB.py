'''

Description:

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

'''





class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        shift = 0
        
        while m != n:
            
            m = m >> 1
            n = n >> 1
        
            shift += 1
        
        
        return m << shift



# m, n : input number pair

## Time Complexity: O( 1 )
#
# Description has guarantees the upper bound of input, thus the time complexity is of O( 1 ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for bitwise operation



def test_bench():

    test_data = [
                    (5, 7),
                    (30, 63),
                    (2**20, 2**20+7)
                ]

    for m, n in test_data:
        print( Solution().rangeBitwiseAnd(m, n) )

    return 



if __name__ == '__main__':
    
    test_bench()