'''

Description:

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.



Example 2:

Input: height = [1,1]
Output: 1



Example 3:

Input: height = [4,3,2,1,4]
Output: 16



Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 3 * 104
0 <= height[i] <= 3 * 104

'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # length of input array
        size = len(height)
        
        # two pointers, left init as 0, right init as size-1
        left, right = 0, size-1
        
        # maximal width between leftmost stick and rightmost stick
        max_width = size - 1
        
        # area also known as the amount of water
        area = 0
        
		# trade-off between width and height
        # scan each possible width and compute maxximal area
        for width in range(max_width, 0, -1):
            
            if height[left] < height[right]:
                # the height of lefthand side is shorter
                area = max(area, width * height[left] )
                
                # update left index to righthand side
                left += 1
                
            else:
                # the height of righthand side is shorter
                area = max(area, width * height[right] )
                
                # update right index to lefthand side
                right -= 1
                
        return area

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration with two-pointers, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index, which is of O( 1 )


import unittest

class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().maxArea( height = [1,8,6,2,5,4,8,3,7] )
        self.assertEqual(result, 49 )

    
    def test_case_2(self):

        result = Solution().maxArea(  height = [1,1] )
        self.assertEqual(result, 1 )

    
    def test_case_3(self):

        result = Solution().maxArea(  height = [4,3,2,1,4] )
        self.assertEqual(result, 16 )


    def test_case_4(self):

        result = Solution().maxArea( height = [1,2,1] )
        self.assertEqual(result, 2)


if __name__ == '__main__':

    unittest.main()