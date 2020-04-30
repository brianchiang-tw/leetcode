'''

Description:

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

'''



class Solution:
    def isHappy(self, n: int) -> bool:
        
        self.table = {}
        

        # Compute the sum of digit square
        def digit_sum( n ):
            
            if n in self.table:
                return self.table[n]
            
            sum_of_digit_square = 0
            
            while n :
                
                sum_of_digit_square += (n % 10)**2
                
                n //= 10
                
            self.table[n] = sum_of_digit_square
            return sum_of_digit_square
        
        
        slow, fast = n, n
        
        # Use cycle detection for happy number judgement
        while True:
            
            slow, fast = digit_sum(slow), digit_sum(fast)
            fast = digit_sum( fast )
            
            if slow == 1 or fast == 1:
                return True
            
            if slow == fast:
                return False



# n : the number of input value

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for loop index and temporary variable, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'n')
def test_bench():

    test_data = [
                    TestEntry( n = 19),
                    TestEntry( n = 20),
                    TestEntry( n = 21),
                    TestEntry( n = 22),
                    TestEntry( n = 23),
                    TestEntry( n = 24),
                    TestEntry( n = 25),
                ]                



    # expected output:
    '''
    True
    False
    False
    False
    True
    False
    False
    '''

    for t in test_data:
        print( Solution().isHappy( n = t.n) )

    return



if __name__ == '__main__':

    test_bench()