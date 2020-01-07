'''

Description:

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

'''



import re

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num == 1:
            return True
        else:
            regex = r'([0]*)$'
            pattern = re.compile(regex)
            
            binary_bit_string = '{0:b}'.format(num)
            
            result = pattern.findall(binary_bit_string)
            
            count_of_1 = binary_bit_string.count('1')
            len_of_tail_0s = len( result[0] )
            
            if len_of_tail_0s and len_of_tail_0s % 2 == 0 and count_of_1 == 1:
                return True
            else:
                return False
            


# n : the value of input number

## Time Complexity: ( n )
#
# The overhead in time is the tail zero finding, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for regex operation, which of O( 1 )



def test_bench():

    test_data = [1, 2, 3, 4, 15, 16, 17, 32, 63,64,65, 1024]

    # expected output:
    '''
    True
    False
    False
    True
    False
    True
    False
    False
    False
    True
    False
    True
    '''



    for n in test_data:
        print( Solution().isPowerOfFour(n) )

    return 



if __name__ == '__main__':

    test_bench()