'''

Description:

iven a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

'''



from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if not matrix:
            return 0
        
        h, w = len(matrix), len(matrix[0])
        
		# in-place update
        dp_table = matrix
        
        max_edge_length = 0
        
        for x in range(w):
            matrix[0][x] = int( matrix[0][x] )
        
        for y in range(h):
            matrix[y][0] = int( matrix[y][0] )
        
        for y in range(h):
            for x in range(w):
                
                if y > 0 and x > 0:
                    if matrix[y][x] == '1':

                        matrix[y][x] = 1 + min( matrix[y][x-1], matrix[y-1][x-1], matrix[y-1][x])

                    else:
                        matrix[y][x] = 0

                max_edge_length = max(max_edge_length, matrix[y][x])
            
        return max_edge_length*max_edge_length



# m : the dimension of column of matrix
# m : the dimension of row of matrix

## Time Complexity: O( m * n )
#
# The overhead in time is the nested loops, which is of O( m * n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index, which is of O( 1 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'matrix')

def test_bench():

    test_data = [   
                    TestEntry( matrix = 
                        [
                            [ '1', '0', '1', '0', '0'],
                            [ '1', '0', '1', '1', '1'],
                            [ '1', '1', '1', '1', '1'],
                            [ '1', '0', '0', '1', '0']
                        ])
                    ,
                    TestEntry( matrix = 
                        [
                            [ '0', '1', '1', '1'],
                            [ '1', '1', '1', '1'],
                            [ '0', '1', '1', '1'],
                            [ '1', '0', '0', '1']
                        ])
                    ,
                    TestEntry( matrix = 
                        [
                            # empty matrix, corner case                            
                        ])    
                ]

    # expected output:
    '''
    4
    9
    0
    '''

    for t in test_data:

        print( Solution().maximalSquare( matrix = t.matrix ) )
    
    return 



if __name__ == '__main__':

    test_bench()

