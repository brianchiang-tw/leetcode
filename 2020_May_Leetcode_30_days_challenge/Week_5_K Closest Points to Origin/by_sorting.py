'''

Description:

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].



Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000

'''



from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        # sort by the distance to origin, in ascending order
        points.sort( key = lambda point: point[0]**2 + point[1]**2 )
        
        return points[:K]



# n : the length of list

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is of O( n log n )

## Space Complexity: O( k )
#
# The overhead in space is the storage for ouput list, points[:K], which is of of O( k )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'points K')
def test_bench():

    test_data = [
                    TestEntry( points = [[1,3],[-2,2]], K = 1 ),
                    TestEntry( points = [[3,3],[5,-1],[-2,4]], K = 2 ),
                ]

    # expected output:
    '''
    [[-2, 2]]
    [[3, 3], [-2, 4]]
    '''

    for t in test_data:
        
        print( Solution().kClosest( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()