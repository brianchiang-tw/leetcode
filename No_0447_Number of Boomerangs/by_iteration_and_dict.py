'''

Description:

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

'''



from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        counter_of_boomerangs = 0
        
        for point_1 in points:
            
            x1, y1 = point_1
            
            distance_count_dict = defaultdict( int )
            
            
            for point_2 in points:
                
                x2, y2 = point_2
                
                diff_x = x2-x1
                diff_y = y2-y1
                
                dist = diff_x ** 2 + diff_y ** 2
                
                distance_count_dict[ dist ] += 1
                
            
            # accumulate the count of boomerang, set i = point_1
            for d in distance_count_dict:
                
                n = distance_count_dict[d]
                
                counter_of_boomerangs += n * (n-1)
                
        
        return counter_of_boomerangs



# n : the length of input list, points

## Time Complexity: O( n ^ 2 )
#
# The overhead in time is the nested loops, which is of O( n ^ 2 ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for the dictionary, distance_count_dict, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'points')
def test_bench():

    test_data = [
                    TestEntry( points = [[0,0],[1,0],[2,0]] )
                ]


    # expected output:
    '''
    2
    '''

    for t in test_data:

        print( Solution().numberOfBoomerangs( points = t.points ) )

    return



if __name__ == '__main__':

    test_bench()