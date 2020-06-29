'''

Description:

Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500



Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000)/1= 2000



Example 3:

Input: salary = [6000,5000,4000,3000,2000,1000]
Output: 3500.00000



Example 4:

Input: salary = [8000,9000,2000,3000,6000,1000]
Output: 4750.00000
 

Constraints:

3 <= salary.length <= 100
10^3 <= salary[i] <= 10^6
salary[i] is unique.
Answers within 10^-5 of the actual value will be accepted as correct.

'''


from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        
        # compute summation excluding max and min value
        summation = sum(salary) - max(salary) - min(salary)
        
        # compute length excluding max and min
        length = len(salary) - 2
        
        # compute average
        return summation/length


# n : the length of input list, salary.

## Time Complexity: O( n )
#
# The overhead of time is the cost of summation and max/min value finding, which are of O( n )

## Space Complexity: O( 1 )
#
# The overhead of space is the storage of temporary variable, which is of O( 1 )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1(self):

        result = Solution().average( salary = [4000,3000,1000,2000] )
        self.assertEqual( result, 2500.00000)



    def test_case_2(self):
    
        result = Solution().average( salary = [1000,2000,3000] )
        self.assertEqual( result, 2000.00000)



    def test_case_3(self):
        
        result = Solution().average( salary = [6000,5000,4000,3000,2000,1000] )
        self.assertEqual( result, 3500.00000)



    def test_case_4(self):
        
        result = Solution().average( salary = [8000,9000,2000,3000,6000,1000] )
        self.assertEqual( result, 4750.00000)



if __name__ == '__main__':

    unittest.main()