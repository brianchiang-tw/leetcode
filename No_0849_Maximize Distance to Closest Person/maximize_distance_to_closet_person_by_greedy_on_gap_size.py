'''

Description:

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.



Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.



Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.

'''



from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        size = len(seats)
        prev = None
        max_dist = -1
        
        ## Maximize distance by greedy on maximal gap size
        for idx, status in enumerate(seats):
            
            if status == 1:
                
                if prev != None:
                    # update maximal distance by gap bettwen ones' pair in the middle, i.e., [ ..., 1, ..., 1, ... ]
                    max_dist = max( max_dist, (idx-prev)//2)
                else:
                    # update maximal distance by the distance between leftmost 1 and left boundary, i.e., [ 0, ..., 1, ...
                    max_dist = max( max_dist, idx-0 )
                
                # update index of previous 1
                prev = idx
        
        # update maximal distance by the distance between rightmost 1 and right boundary, i.e., [ ..., 1, ..., 0]
        max_dist = max( max_dist, (size-1)-prev)
        
        return max_dist



# n : the length of input array, seats

## Time Compleity: O( n )
#
# The overhead in time is the for loop, iterating on (idx, status), which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and variable for updating max_dist, which is of O( 1 ).


def test_bench():

    test_data = [
                    [1,0,0,0,1,0,1],
                    [1,0,1,0,1,0,1],
                    [0,0,0,1,0,1,0],
                    [0,1,0,1,0,0,0],
                    [1,0,0,0],
                    [0,0,0,1],
                    [1,0,0,1]
                ]

    for seat_sequence in test_data:

        print( Solution().maxDistToClosest(seat_sequence) )
    
    return



if __name__ == '__main__':

    test_bench()