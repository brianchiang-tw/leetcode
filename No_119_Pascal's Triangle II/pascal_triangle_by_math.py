'''

Description:

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

'''


from math import factorial
from typing import List

class Solution:
    
    def comb(self, n, m):
        
        if n == m or m == 0:
            return 1
        else:
            return factorial(n) // ( factorial(m) * factorial(n-m) )

        
    def getRow(self, rowIndex: int) -> List[int]:
        
        # the coefficient of level k is as folling
        #
        # C(k,0), C(k,1), ... , C(k,k)
        
        return [ self.comb(rowIndex,i) for i in range(0, rowIndex+1) ]



# k : the input value of rowIndex

## Time Complexity: O( k ) 
#
# The major overhead in time is the length of list comprehension on i, which is of O( k )

## Space Complexity: O( k )
#
# The major overhead in space is the storge for output list, which is of O( k )




def test_bench():

    test_data = [ 0, 1, 2, 3, 4, 5 ]

    # expected output:
    '''
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    '''

    for n in test_data:

        print( Solution().getRow(n) )

    return



if __name__ == '__main__':

    test_bench()