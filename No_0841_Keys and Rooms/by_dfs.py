'''

Description:

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.



Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.

'''



from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
		
		# a set to record visited rooms
        visited = set()
        
        # --------------------------------
        def dfs( cur_room ):
            
            if cur_room in visited:
			
				# base case aslo known as stop condition
                return
            
			# mark current room as visited
            visited.add( cur_room )
            
			# general case:
            for next_room in rooms[cur_room]:
				
				# Visit next room in DFS
                dfs( next_room )
            
            return
        # --------------------------------
        
		# Launch DFS at room_#0
        dfs(cur_room = 0)
        
		# Return true if all rooms are visited
        return len(visited) == len(rooms)



# n : the number of rooms
# k : the average number of keys per room

## Time Complexity: O( n * k )
#
# The overhead in time is the while loop, iterating on available_room, which if of O( n ),
# and the for loop, iterating on room_idx_with_key, which is of O( k )
#
# It takes O( n * k ) in total.


## Space Complexity: O( n )
#
# The overhead in space is the storage for recursion call stack, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().canVisitAllRooms( rooms = [[1],[2],[3],[]] )
        self.assertEqual(result, True )
    


    def test_case_2( self ):

        result = Solution().canVisitAllRooms( rooms = [[1,3],[3,0,1],[2],[0]] )
        self.assertEqual(result, False )
    




if __name__ == '__main__':

    unittest.main()