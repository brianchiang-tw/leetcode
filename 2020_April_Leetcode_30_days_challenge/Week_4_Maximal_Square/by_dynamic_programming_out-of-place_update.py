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
        
        dp_table = [ [ int(x) for x in row] for row in matrix]
        
        h, w = len(matrix), len(matrix[0])
        
        max_edge_of_square = 0
        
        for y in range(h):
            for x in range(w):
                
                if y and x and int(matrix[y][x]):
                    dp_table[y][x] = 1 + min( dp_table[y][x-1], dp_table[y-1][x-1], dp_table[y-1][x] )
                
                max_edge_of_square = max(max_edge_of_square, dp_table[y][x])
        

        return max_edge_of_square*max_edge_of_square



# m : the dimension of column of matrix
# m : the dimension of row of matrix

## Time Complexity: O( m * n )
#
# The overhead in time is the nested loops, which is of O( m * n )

## Space Complexity: O( m * n )
#
# The overhead in space is the storage for dp_table, which is of O( m * n )


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

