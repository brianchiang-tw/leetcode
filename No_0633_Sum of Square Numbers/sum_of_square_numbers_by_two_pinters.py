'''

Description:

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False

'''



from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        # general form:
        # a^2 + b^2 == c where a <= b
        
        a = 0
        b = int( sqrt(c) )
        
        while a <= b:
            
            trial = a ** 2 + b ** 2
            
            if trial < c:
                a += 1
            elif trial > c:
                b -= 1
            else:
                return True
            
        
        return False



# n : the input value

## Time Complexity: O( sqrt( n ) )
#
# The overhead in time is the loop iterating on a <= b, which is of O( sqrt(n) ).

## Space Complexity: O( 1 )
#
# The overhead in space is the looping index and a, b for computation, which is of O( 1 ).




def test_bench():

    test_data = [3, 5, 13, 25, 18, 28, 33]

    # expected output:
    '''
    False
    True
    True
    True
    True
    False
    False    
    '''

    for number in test_data:

        print( Solution().judgeSquareSum(number) )
    
    return 



if __name__ == '__main__':

    test_bench()