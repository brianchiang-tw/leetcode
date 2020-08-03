'''

Description:

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

'''


# Time Complexity: O( 1 )
#
# The overhead in time is the cost of formula computation, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 )



class Solution:
    def addDigits(self, num: int) -> int:
        
        if num < 10:
            # single digit
            return num
			
        else:
            # multiple digits, using the formula of digital root
            return (num-1)%9 + 1


import unittest
class Testing(unittest.TestCase):

    def test_case_1(self):

        result = Solution().addDigits(38)
        self.assertEqual(result, 2)

    
    def test_case_2(self):

        result = Solution().addDigits(105)
        self.assertEqual(result, 6)

    
    def test_case_3(self):

        result = Solution().addDigits(99)
        self.assertEqual(result, 9)



if __name__ == '__main__':

    unittest.main()
