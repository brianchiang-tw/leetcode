'''

Description:

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

'''


class Solution:
    
    def __init__(self):
        
        self.cache = {}
    
    def climbStairs(self, n: int) -> int:    
        
        if n in self.cache:
            return self.cache[n]
        
        if n == 0 or n == 1:
            return 1
        
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.cache[n] = result
            return result


# n : the value of input n

## Time Complexity: O( n )
#
# The overhead in time is the recursion depth of recursion, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the recursion depth of recursion, which is of O( n )

import unittest
class Testing(unittest.TestCase):

  def test_case_1(self):

    result = Solution().climbStairs(2)
    self.assertEqual(result, 2)


  def test_case_2(self):

    result = Solution().climbStairs(3)
    self.assertEqual(result, 3)


  def test_case_3(self):

    result = Solution().climbStairs(4)
    self.assertEqual(result, 5)



if __name__ == '__main__':

  unittest.main()
