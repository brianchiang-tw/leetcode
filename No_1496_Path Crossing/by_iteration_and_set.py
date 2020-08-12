'''

Description:

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. Return False otherwise.

 

Example 1:

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.



Example 2:

Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 10^4
path will only consist of characters in {'N', 'S', 'E', 'W}

'''



class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        cur_point, next_point = (0, 0), None
        path_tracking = set( [ cur_point ] )
        
        for p in path:
            
            cur_x, cur_y = cur_point
            
            if 'N' == p:
                cur_y += 1
            
            elif 'E' == p:
                cur_x += 1
                
            elif 'W' == p:
                cur_x -= 1
                
            elif 'S' == p:
                cur_y -= 1
            
            next_point = ( cur_x, cur_y )
            if next_point in path_tracking:
                # now, it is of path crossing
                return True
            
            # add next point into path tracking set
            path_tracking.add( next_point )
            
            # move to next point
            cur_point = next_point
        
        # no path crossing
        return False
                


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().isPathCrossing(path = "NES")
        self.assertEqual(result, False)


    def test_case_2( self ):
    
        result = Solution().isPathCrossing(path = "NESWW")
        self.assertEqual(result, True)



if __name__ == '__main__':

    unittest.main()