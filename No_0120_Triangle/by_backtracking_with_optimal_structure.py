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
        
        # backtracking from bottom level to top level
        min_cost = [ *triangle[-1] ]
        
        # update min cost
        for y in reversed( range(0, h-1) ):
            for x in range(y+1):
                min_cost[x] = triangle[y][x] + min( min_cost[x], min_cost[x+1])
                
        return min_cost[0]



# m : the hight of triangle
# n : the base width of triangle

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of nested for loop, which is of O( m*n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for min cost array, which is of O( n ).

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