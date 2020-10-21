'''

Description:

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.



Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.



Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.



Example 4:

Input: asteroids = [-2,-1,1,2]
Output: [-2,-1,1,2]
Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
 

Constraints:

1 <= asteroids <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
   Hide Hint #1  
Say a row of asteroids is stable. What happens when a new asteroid is added on the right?

'''

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        # scan each star
        for star in asteroids:
            
            stack.append( star )
            
            # check for possible collision
            while len(stack) >= 2:
                
                # one pair of stars, a and b collide
                if stack[-2] > 0 and stack[-1] < 0:
                    
                    a = stack.pop()
                    b = stack.pop()
                    
                    if a + b:
                        # a and b have different size, the bigger one remains
                        stack.append( max(a, b, key = abs) )
                        
                else:
                    
                    # exit checking while loop
                    break
                    
        return stack


# n : the length of asteroids

## Time Complexity: O( n )
#
# The overhead in time is the cost of for-loop with stack, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for stack, which is of O( n )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().asteroidCollision( asteroids=[5,10,-5] )
        self.assertEqual(result, [5, 10])

    
    def test_case_2( self ):

        result = Solution().asteroidCollision( asteroids=[8,-8] )
        self.assertEqual(result, [])


    def test_case_3( self ):

        result = Solution().asteroidCollision( asteroids=[10,2,-5] )
        self.assertEqual(result, [10])


    def test_case_4( self ):

        result = Solution().asteroidCollision( asteroids=[-2,-1,1,2] )
        self.assertEqual(result, [-2,-1,1,2])    


if __name__ == '__main__':

    unittest.main()        