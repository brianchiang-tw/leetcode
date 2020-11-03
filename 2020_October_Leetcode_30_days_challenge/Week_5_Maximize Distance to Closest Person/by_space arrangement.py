'''

Description:

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

 

Example 1:


Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.



Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.



Example 3:

Input: seats = [0,1]
Output: 1
 

Constraints:

2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.

'''


from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        person_idx = None
        last_idx = len(seats)-1
        
        dist = 0
        
        # sacn for each seats
        for cur_idx, seat in enumerate(seats):
            
            # this seat is taken by someone
            if seat == 1:
                
                if person_idx is None:
                    # No person on the left, Alex seat on left hand side
                    dist = max(dist, cur_idx)

                else:
                    # Surrounded by two person, Alex seat on the middle
                    dist = max(dist, (cur_idx-person_idx) // 2)
                
                person_idx = cur_idx
        
        # No person on the right, Alex seat on the right hand side
        dist = max(dist, last_idx-person_idx)
        
        return dist



# n :the length of seats

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 )


import unittest

class TestClass( unittest.TestCase):

    def test_case_1( self ):

        result = Solution().maxDistToClosest( seats=[1,0,0,0,1,0,1] )
        self.assertEqual(result, 2)

    
    def test_case_2( self ):
        result = Solution().maxDistToClosest( seats=[1,0,0,0] )
        self.assertEqual(result, 3)


    def test_case_3( self ):
        result = Solution().maxDistToClosest( seats=[0,1] )
        self.assertEqual(result, 1)


if __name__ == '__main__':

    unittest.main()       