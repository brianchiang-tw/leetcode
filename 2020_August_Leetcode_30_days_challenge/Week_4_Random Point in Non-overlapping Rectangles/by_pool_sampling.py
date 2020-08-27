'''

Description:

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.



Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]



Example 2:

Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.

'''



from random import randint
from bisect import bisect_left

class Solution:

    def __init__(self, rects: List[List[int]]):
        
        self.rectangles = rects
        
        # record prefix sum of points number (i.e., acts like the CDF)
        self.prefix_points_sum = []
        
        for x1, y1, x2, y2 in rects:
            
            # compute current number of points
            cur_points = ( x2 - x1 + 1 ) * ( y2 - y1 + 1)
            
            # update to prefix table
            if self.prefix_points_sum:
                self.prefix_points_sum.append( self.prefix_points_sum[-1] + cur_points )
                
            else:
                self.prefix_points_sum.append( cur_points )
        
            

    def pick(self) -> List[int]:
        
        total_num_of_points = self.prefix_points_sum[-1]
        
        # get a random point serial, sampling from 1 ~ total number of points
        random_point_serial = randint(1, total_num_of_points)
        
        # get the rectangle index by looking up prefix table with bisection
        idx_of_rectangle = bisect_left(self.prefix_points_sum, random_point_serial)
        
        # get the point range of that rectangle by index
        x1, y1, x2, y2 = self.rectangles[idx_of_rectangle]
        
        # compute the offset value between prefix sum and random point serial
        offset = self.prefix_points_sum[idx_of_rectangle] - random_point_serial
        
        # compute corresponding x, y points coordination in that rectangle
        x = offset % ( x2 - x1 + 1) + x1
        y = offset // ( x2 - x1 + 1) + y1
        
        return [x, y]   


# This is a problem with random output everytime, therefore local testbench is not provided here.
