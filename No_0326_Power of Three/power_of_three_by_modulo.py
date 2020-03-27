'''

Description:

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true



Example 2:

Input: 0
Output: false



Example 3:

Input: 9
Output: true



Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?

'''



from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n <= 0: 
            return False
        else:
            return ((3 ** 19) % n ) == 0






# n : the input value

## Time Complexity: O( log n )
#
# The overhead in time is the cost of logarithm, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the cost of temporarily variable, which is of O( 1 )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'n')
def test_bench():

    test_data = [
                    TestEntry( 27 ),
                    TestEntry( 0 ),
                    TestEntry( 9 ),
                    TestEntry( 45 ),
                ]
    

    # expected output:
    '''
    True
    False
    True
    False
    '''

    for t in test_data:
        print( Solution().isPowerOfThree( n = t.n) )

    return



if __name__ == '__main__':

    test_bench()