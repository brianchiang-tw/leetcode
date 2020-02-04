'''

Description:

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.



Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101



Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.



Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.



Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.

'''



class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        # convert to binary bit string, discard '0b' prefix
        bit_string = bin(n)[2:]
        
        set_of_odd_digits = set( bit_string[1: :2] )
        set_of_even_digits = set( bit_string[0: : 2] )
        
        alternaing_bits_flag = set_of_odd_digits != set_of_even_digits and len(set_of_odd_digits) <= 1 and len(set_of_even_digits) <= 1
        
        return alternaing_bits_flag



# n : the value of input 

## Time Complexity: O( log n )
#
# The overhead in time is the cost of bit string conversion, which is of O( log n )


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for bit string, which is of O( log n )


def test_bench():

    test_data = [5,7,11,10]

    # expected output:
    '''
    True
    False
    False
    True
    '''

    for number in test_data:

        print( Solution().hasAlternatingBits(number) )
    
    return 



if __name__ == '__main__':

    test_bench()