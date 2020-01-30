'''

Description:

Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.

 

Example 1:

Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.



Example 2:

Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.



Example 3:

Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Note:

0 <= N < 10^9

'''



class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        # convert to binary bit string, and dicard '0b' prefix
        bit_string = bin(N)[2:]
        
        # make complement by 0/1 -> 1/0 mapping
        complement =bit_string.translate( str.maketrans('01','10') ) 
        
        # convert bit string to decimal integer
        return int( complement, 2)



# n : the input value of N.

## Time Complexity: O( log n )
#
# The overhead in time is the binary bits length of n, which is of O( log n ).

## Space Complexity: O( log n )
#
# The overhead in space is the storage for binary bit string, which is of O( log n)



def test_bench():

    test_data = [
                    0,
                    1,
                    5,
                    7,
                    10
                ]

    # expected output:
    '''
    1
    0
    2
    0
    5
    '''


    for number in test_data:

        print( Solution().bitwiseComplement(number) )
    
    return



if __name__ == '__main__':
    
    test_bench()