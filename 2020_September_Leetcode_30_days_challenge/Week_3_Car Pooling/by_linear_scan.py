'''

Description:

You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false



Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true



Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true



Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000

'''



from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        stops = [0 for _ in range(1001) ]
        
        for loading, start, end in trips:
            
			# get on car at start
            stops[start] -= loading
			
			# get off car at end 
            stops[end] += loading
            
            
        for loading in stops:
            
            capacity += loading
            
            if capacity < 0:
				# check whether capacity is enough or not
                return False
            
        return True



# n : the length of trips

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the cost of stops array, which is of O( 1001 ) = O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().carPooling( trips = [[2,1,5],[3,3,7]], capacity = 4 )
        self.assertEqual(result, False )


    def test_case_2( self ):

        result = Solution().carPooling( trips = [[2,1,5],[3,3,7]], capacity = 5 )
        self.assertEqual(result, True )        


    def test_case_3( self ):

        result = Solution().carPooling( trips = [[2,1,5],[3,5,7]], capacity = 3 )
        self.assertEqual(result, True)


    def test_case_4( self ):

        result = Solution().carPooling( trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11 )
        self.assertEqual(result, True)


if __name__ == '__main__':

    unittest.main()