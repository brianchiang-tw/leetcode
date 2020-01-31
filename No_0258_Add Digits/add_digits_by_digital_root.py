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



class Solution:
    def addDigits(self, num: int) -> int:
        
        if num < 10:
            # single digit
            return num
        else:
            # multiple digits
            return (num-1)%9 + 1



# n : the input value of num

## Time Complexity: O( 1 )
#
# The overhead in time is the cost of formula computation, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the variable of arithmetic computation, which is of O( 1 )


def test_bench():

    test_data = [0,1,9,10,11,33,66,99,100,101,999,1000,1001]

    # expected output:
    '''
    0
    1
    9
    1
    2
    6
    3
    9
    1
    2
    9
    1
    2    
    '''

    for number in test_data:
        print( Solution().addDigits(number) )
    
    return



if __name__ == '__main__':

    test_bench()