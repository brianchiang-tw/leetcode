'''

Description:

We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.



Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3



Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000

'''


from typing import List

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        # padding one dummy -1 to represent empty list
        A = [ -1 ] + A
        B = [ -1 ] + B
        
        h, w = len(A), len(B)
        dp_table = [ [ 0 for _ in range(w) ] for _ in range(h) ]
        
        
        
        for y in range(1, h):
            for x in range(1, w):
                
                if A[y] == B[x]:
                    # current number is matched, add one more uncrossed line
                    dp_table[y][x] = dp_table[y-1][x-1] + 1
                    
                else:
                    # cuurent number is not matched, backtracking to find maximal uncrossed line
                    dp_table[y][x] = max( dp_table[y][x-1], dp_table[y-1][x] )

                    
        return dp_table[-1][-1]



# m : the length of input list A
# n : the length of input list B

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of nested loop, which is of O( m*n )

## Space Complexity: O( m*n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( m*n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'A B')

def test_bench():

    test_data = [
                    TestEntry( A = [1,4,2], B = [1,2,4] ),
                    TestEntry( A = [2,5,1,2,5], B = [10,5,2,1,5,2] ),
                    TestEntry( A = [1,3,7,1,7,5], B = [1,9,2,5,1] ),
                ]

    # expected output:
    '''
    2
    3
    2
    '''

    for t in test_data:

        print( Solution().maxUncrossedLines( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()