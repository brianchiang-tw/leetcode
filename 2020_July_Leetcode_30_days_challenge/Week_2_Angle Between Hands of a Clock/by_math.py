'''

Description:

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:

Input: hour = 12, minutes = 30
Output: 165



Example 2:

Input: hour = 3, minutes = 30
Output: 75



Example 3:

Input: hour = 3, minutes = 15
Output: 7.5



Example 4:

Input: hour = 4, minutes = 50
Output: 155



Example 5:

Input: hour = 12, minutes = 0
Output: 0
 

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.

Hint #1  
The tricky part is determining how the minute hand affects the position of the hour hand.

Hint #2  
Calculate the angles separately then find the difference.

'''



class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # compute degree for hour and minutes
        deg_of_hour = hour * (360 / 12) % 360 + 30 * (minutes / 60)
        deg_of_min = minutes * ( 360 / 60 )
        
        # get maximal degree and minimal degree
        max_degree, min_degree = max(deg_of_hour, deg_of_min), min(deg_of_hour, deg_of_min)
        
        # compute the angle of the smaller one
        diff = min(max_degree - min_degree, 360 + min_degree - max_degree)
        
        return diff



## Time Complexity: O( 1 )
#
# The overhead in time is the cost of basic math calculation, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):
        result = Solution().angleClock( hour = 12, minutes = 30 )
        self.assertEqual(result, 165)


    def test_case_2(self):
        result = Solution().angleClock( hour = 3, minutes = 30 )
        self.assertEqual(result, 75)


    def test_case_3(self):
        result = Solution().angleClock( hour = 3, minutes = 15 )
        self.assertEqual(result, 7.5)


    def test_case_4(self):
        result = Solution().angleClock( hour = 4, minutes = 50 )
        self.assertEqual(result, 155)


    def test_case_5(self):
        result = Solution().angleClock( hour = 12, minutes = 0 )
        self.assertEqual(result, 0)



if __name__ == '__main__':

    unittest.main()

        