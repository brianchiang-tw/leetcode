'''

Description:

A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.



Example 1:

Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.



Example 2:

Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.



Example 3:

Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.



Constraints:

1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4


'''



from typing import List
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        if start == destination :
            # Quick response for the same bus stop
            return 0
        
        
        # distance AB = distance BA
        # Let start < destination for convenience 
        start, destination = min(start, destination), max(start, destination)

        
        # path length in clockwise
        clockwise = sum( distance[ start : destination ] )
        
        # path length in counter clockwise
        counter_clockwise = sum( distance[ destination:]) + sum( distance[ :start] )
        
        return min( clockwise, counter_clockwise )



def test_bench():

    test_data = [
                    ([1,2,3,4], 0, 0),
                    ([1,2,3,4], 0, 1),
                    ([1,2,3,4], 0, 2),
                    ([1,2,3,4], 0, 3),
                    ([1,2,3,4], 1, 2),
                    ([1,2,3,4], 2, 1),
                    ([1,2,3,4], 2, 3),
                    ([1,2,3,4], 3, 2)
                ]

    # expected output:
    '''
    0
    1
    3
    4
    2
    2
    3
    3
    '''


    for bus_stops_distance, start, dest in test_data:

        print( Solution().distanceBetweenBusStops(bus_stops_distance, start, dest) )
    
    return 



if __name__ == '__main__':

    test_bench()

