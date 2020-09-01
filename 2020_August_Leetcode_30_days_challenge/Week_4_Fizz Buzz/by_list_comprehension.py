'''

Description:

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

'''

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        # list comprehension with string rule of FizzBuzz
        list_of_output = [ 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5 ) or str(i) for i in range(1, n+1) ]
        
        return list_of_output



# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the cost of list comprehension, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage output list, which is of O( n ).

import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().fizzBuzz(9)
        self.assertEqual(result, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz'])


    def test_case_2( self ):

        result = Solution().fizzBuzz(15)
        self.assertEqual(result, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])



if __name__ == '__main__':

    unittest.main()