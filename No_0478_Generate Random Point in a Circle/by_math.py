'''

Description:

Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:

input and output values are in floating-point.
radius and x-y position of the center of the circle is passed into the class constructor.
a point on the circumference of the circle is considered to be in the circle.
randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.



Example 1:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]



Example 2:

Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren't any.

'''

from typing import List
from random import random, seed
from math import pi, cos, sin, sqrt

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):

        self._x_center = x_center
        self._y_center = y_center
        self._r = radius

        # Initialize random seed with system time
        seed()

    
    def randPoint(self) -> List[float]:

        # random theta from 0 to 2 * pi
        rand_theta = random() * 2 * pi

        # random radis from 0 to R
        rand_radius = sqrt( random() ) * self._r

        # compute random point based on polar coordination
        rand_x_coord = rand_radius * cos( rand_theta ) + self._x_center
        rand_y_coord = rand_radius * sin( rand_theta ) + self._y_center

        return [rand_x_coord, rand_y_coord]


# Because this is a problem of randomness, therefore local testbench is not provided

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()