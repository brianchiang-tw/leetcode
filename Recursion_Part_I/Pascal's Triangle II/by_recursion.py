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


from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            # Base case
            return [1]
        
        elif rowIndex == 1:
            # Base case
            return [1, 1]
        
        else:
            # General case:
            last_row = self.getRow( rowIndex-1 )
            size = len(last_row)
            return [ last_row[0] ] + [ last_row[idx] + last_row[idx+1] for idx in range( size-1) ] + [ last_row[-1] ]



# n : the input value of row index

## Time Complexity: O( n^2 )
#
# The overhead in time is the depth of recursion with the cost of computation, which is of O( n ) * O( n ) = O( n^2 )

## Space Complexity: O( n^2 )
#
# The overhead in space is the storage of recursion call stack with the storage of list comprehension, which is of O( n ) * O( n ) = O( n^2 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'row_index')

def test_bench():

    test_data = [
                    TestEntry( row_index = 0 ),
                    TestEntry( row_index = 1 ),
                    TestEntry( row_index = 2 ),
                    TestEntry( row_index = 3 ),
                    TestEntry( row_index = 4 ),
                    TestEntry( row_index = 5 ),
                ]

    # expected output:
    '''
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    '''

    for t in test_data:

        print( Solution().getRow( rowIndex = t.row_index ) )
    
    return



if __name__ == '__main__':

    test_bench()    