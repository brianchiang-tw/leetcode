'''

Description:

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

'''



from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        h = len(triangle)
        
        if h == 1:
            # Quick response for single level
            return triangle[0][0]
        
        global_min_cost_path = float('inf')
        
        # in-place update with optimal substructure
        for y in range(1, h):
            for x in range(y+1):
                
                min_prev = None         
                if x == 0:
                    # left-most grid
                    min_prev = triangle[y-1][x]
                    
                elif x == y:
                    # right-most grid
                    min_prev = triangle[y-1][x-1]
                    
                else:
                    # middle grid
                    min_prev = min( triangle[y-1][x-1], triangle[y-1][x])
                
                # update min cost from top level to current grid
                triangle[y][x] = min_prev + triangle[y][x]
                
                if y == h-1:
                    # update global min cost path from top level to bottom level
                    global_min_cost_path = min( global_min_cost_path, triangle[y][x])

              
                
        return global_min_cost_path



# m : the hight of triangle
# n : the base width of triangle

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of nested for loop, which is of O( m*n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and temporary variable, which is of O( 1 ).

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'triangle')

def test_bench():

    test_data = [   
                    TestEntry( triangle =  
                                    [
                                        [2],
                                        [3,4],
                                        [6,5,7],
                                        [4,1,8,3],
                                    ]
                            ),

                    TestEntry( triangle =  
                                    [
                                        [1],
                                        [2,3],
                                        [4,5,6],
                                        [7,8,9,10],
                                    ]
                            ),                            

                    TestEntry( triangle =  
                                    [
                                        [-10],
                                    ]
                            ),                   
                ]        

    # expected output:
    '''
    11
    14
    -10
    '''

    for t in test_data:

        print( Solution().minimumTotal( triangle = t.triangle) )

    return



if __name__ == '__main__':

    test_bench()