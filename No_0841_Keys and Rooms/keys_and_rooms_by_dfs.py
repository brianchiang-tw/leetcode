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
        
        size = len( rooms )
        
        # flag table:
        # index   : room index, from 0 to size-1
        # value : True for opened and visited, False for locked
        room_visit_table = [ False for i in range(size) ]
        
        
        # all room are locked except for room_#0 is opened
        room_visit_table[0] = True
        
        # room_#0 is initialized to be opened
        available_room = set( [0] )
        
        
        while available_room:

            # Pop one room from set: available_room 
            currnet_room = available_room.pop()
            
            # Open and update current room as opened and visited
            room_visit_table[currnet_room] = True

            # Scan each key, and
            # add those room_idx_with_key to available_room, if they are not visited yet.
            for room_idx_with_key in rooms[currnet_room]:
                
                if not room_visit_table[room_idx_with_key]:
                    available_room.add( room_idx_with_key )
            
            
        # if all room is visited and opened, then return True
        return all(room_visit_table)



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
# The overhead in space is the storage for room_visit_table, and available_room, which are of O( n ).



def test_bench():

    test_data = [
                    #[[1],[2],[3],[]],
                    [[1,3],[3,0,1],[2],[0]]
                ]

    for room_sequence in test_data:
        print( Solution().canVisitAllRooms(room_sequence) )

    return



if __name__ == '__main__':

    test_bench()