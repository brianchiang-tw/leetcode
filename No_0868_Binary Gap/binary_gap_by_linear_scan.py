'''

Description:


Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.



Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.



Example 3:

Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.



Example 4:

Input: 8
Output: 0
Explanation: 
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 

Note:

1 <= N <= 10^9

'''


class Solution:
    
    
    def binaryGap(self, N: int) -> int:
        
        def to_binary( n ):
            
            # convert integer to bit string, and
            # discard binary prefix '0b'
            return bin(n)[2:]
        
        # convert integer to binary bit string
        bits_string = to_binary(N)
        
        # Quick response for corner case
        if bits_string.count('1') <= 1:
            return 0
        
        max_gap = 0
        
        prev_index = None
        for cur_index, digit in enumerate(bits_string):
            
            if digit == '1':
                
                if prev_index is not None:
                    # update max gap
                    max_gap = max( max_gap, cur_index - prev_index )
                
                # update prev index of '1'
                prev_index = cur_index
            
        
        return max_gap



# n : the input value of N

## Time Complexity: O( log n )
#
# The overhead in time is the for loop, iterating on (cur_index, digit), which is of O( log n)

## Space Complexity: O( log n )
#
# The overhead in space is the storage for bits_string, which is of O( log n )


def test_bench():

    test_data = [
                    22, 5, 6, 8
                ]

    # expected output:
    '''
    2
    2
    1
    0
    '''

    for number in test_data:

        print( Solution().binaryGap(number) )
    
    return 



if __name__ == '__main__':

    test_bench()