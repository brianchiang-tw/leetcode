'''

Description:

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000



Example 2:

Input: 2.10000, 3
Output: 9.26100



Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

'''



class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            # Base case:
            return 1.0
        
        elif n == 1:
            # Base case:
            return x
        
        elif n < 0:
            # General case:
            # x ^ (-n) = (1/x) ^ n
            return  self.myPow( 1/x, -n)
        
        
        # Recurrence of fast power
        
        if n & 1:
            return x * self.myPow( x*x, n // 2)
        else:
            return self.myPow( x*x, n // 2)



# n : the value of power

## Time Complexity: O( log n )
#
# The overhead in time is the cost of recursion with divide-and-conquer, which is of O( log n )

## Space Complexity: O( log n )
#
# The overhead in space is the storage for recursion call stack, which is of O( log n )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().myPow(2, 10)
        self.assertEqual(result, 1024.00000)


    def test_case_2(self):

        result = Solution().myPow(2, 3)
        self.assertEqual(result, 8.00000)


    def test_case_3(self):

        result = Solution().myPow(2, -2)
        self.assertEqual(result, 0.25000)



if __name__ == '__main__':

    unittest.main()