'''

Description:

Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x,y) == z.

The function is constantly increasing, i.e.:

f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
The function interface is defined like this: 

interface CustomFunction {
public:
  // Returns positive integer f(x, y) for any given positive integer x and y.
  int f(int x, int y);
};
For custom testing purposes you're given an integer function_id and a target z as input, where function_id represent one function from an secret internal list, on the examples you'll know only two functions from the list.  

You may return the solutions in any order.

 

Example 1:

Input: function_id = 1, z = 5
Output: [[1,4],[2,3],[3,2],[4,1]]
Explanation: function_id = 1 means that f(x, y) = x + y



Example 2:

Input: function_id = 2, z = 5
Output: [[1,5],[5,1]]
Explanation: function_id = 2 means that f(x, y) = x * y
 

Constraints:

1 <= function_id <= 9
1 <= z <= 100
It's guaranteed that the solutions of f(x, y) == z will be on the range 1 <= x, y <= 1000
It's also guaranteed that f(x, y) will fit in 32 bit signed integer if 1 <= x, y <= 1000

'''



"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""



class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        solution_pair = []
        
        x, y = 1, z
        
        while x <= z and y >= 1:
            
            f_of_x_y = customfunction.f(x,y)
            
            if f_of_x_y > z:
                # this f(x,y) too big, make it smaller
                y -= 1
                
            elif f_of_x_y < z:
                # this f(x,y) too small, make it bigger
                x += 1
            
            else:
                # pair (x, y) is a solution to f(x,y) = z
                solution_pair.append( (x,y) )
                x += 1
        
        return solution_pair



# n : the number of z

## Time Complexity: O( n )
#
# The overhead in time is the while loop iterating on (x,y), which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for all solution pairs( n )