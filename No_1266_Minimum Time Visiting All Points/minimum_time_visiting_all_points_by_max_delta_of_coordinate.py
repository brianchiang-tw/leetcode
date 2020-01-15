'''

Description:

On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.


Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5
 

Constraints:

points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000

'''



from typing import List
class Solution:
    
    def shortest_dist( self, p1, p2 ):
    
        x1, y1 = p1
        x2, y2 = p2
        
        # any two points can be connected by combination of '-', '|', '／', '＼'
        # shortest distance between p1 and p2 
        # = the path between p1 and p2 with lowest cost 
        #
        #
        # Denote max( delta x, delta y ) as M
        # and min( delta x, delta y ) as n
        #
        # shortest path = n diagonal walks + (M-n) vertical or horizontal walks
        #               = M walks in total
        #               = max( delta x, delta y )
        
        return max( abs(y1-y2), abs(x1-x2) )
    
    
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        shortest_path = 0

        # traverse each point pairs with lowest cost
        for i in range(len(points)-1 ):
        
            shortest_path += self.shortest_dist( points[i], points[i+1] )
            
        return shortest_path
            


# n : the length of input list, points.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and min-max operation, which is of O( 1 ).


def test_bench():

    test_data = [
                    [[1,1],[3,4],[-1,0]],
                    [[3,2],[-2,2]]
                ]

    # expected output:
    '''
    7
    5
    '''

    for list_of_points in test_data:

        print( Solution().minTimeToVisitAllPoints(list_of_points) )
    
    return 



if __name__ == '__main__':

    test_bench()