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



class Solution:
    def isPowerOfFour(self, num):
        
        if num < 1: 
            return False
        
        elif num ==1 : 
            return True
        
        else:
            # Capture all (2^n)^k, by num & (num-1) == 0
            # Then screen out those numbers which are exact power of two only by 0xAAAAAAAA mask
            # Finally, we have number of (2^n)^k, where k >= 2
            return num & (num-1) == 0 and num & 0xAAAA_AAAA == 0



# n : the value of input number

## Time Complexity: ( log n )
#
# The overhead in time is the bitwise operation, which is of O( log n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for bitwise operation, which of O( 1 )



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