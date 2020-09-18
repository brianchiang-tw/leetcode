'''

Description:

On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.



Example 2:

Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.


Example 3:

Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Note:

1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}

Hint #1  
Calculate the final vector of how the robot travels after executing all instructions once - it consists of a change in position plus a change in 

Hint #2  
The robot stays in the circle iff (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.

'''



class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        # direction vector
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        NORTH = 0 # WEST = 1, SOUTH = 2, EAST = 3
        
        # origin point
        x, y = 0, 0
        
        # initial direction
        cur_direction = NORTH
        
        for i in instructions:
            
            if i == "G":
                
                # go one step
                x += dirs[cur_direction][0]
                y += dirs[cur_direction][1]
                
                
            elif i == "L":
                
                # turn left
                cur_direction = (cur_direction + 1) % 4
                
                
            elif i == "R":
                
                # turn right
                cur_direction = (cur_direction - 1) % 4
        
        
        # Check if either go back to origin, or not face to North
        return (x == 0 and y == 0) or (cur_direction != NORTH)



# n : the length of instructions

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop iteration, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().isRobotBounded( instructions="GGLLGG" )
        self.asssertEqual(result, True)


    def test_case_2( self ):

        result = Solution().isRobotBounded( instructions="GG" )
        self.asssertEqual(result, False)


    def test_case_3( self ):

        result = Solution().isRobotBounded( instructions="GL" )
        self.assertEqual(result, True)        



if __name__ == '__main__':

    unittest.main()        