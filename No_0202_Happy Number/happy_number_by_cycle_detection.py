'''

Description:

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''


from typing import List
class Solution:

    def digit_sum(self, n:int) -> int:
        
        sum_digit_square = 0
        
        while n > 0:
            
            digit = n % 10
            
            sum_digit_square += int( digit ** 2 )
            
            n = n // 10
            
        return sum_digit_square



    def isHappy(self, n: int) -> bool:
        
        slow, fast = n, n
        
        while True:
            
            slow = self.digit_sum( slow )
            
            fast = self.digit_sum( fast )
            fast = self.digit_sum( fast )
            
            if slow == 1 or fast == 1:
                # happy number
                return True
            
            if slow == fast:
                # non-happy number, fall in dead cycle.
                return False


# n : the input value of n

## Time Complexity: O( n )
#
# The overhead in time is the while loop iterating on (slow, fast), which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in spce is the storage for double pointers and digit square sum, which is of O( 1 ).



def test_bench():

    test_data = [19,20,21,22,23,24,25]

    for n in test_data:
        
        print( Solution().isHappy(n) )
    
    return


if __name__ == '__main__':

    test_bench()