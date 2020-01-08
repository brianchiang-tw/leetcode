'''

Description:

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.


'''



class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
    
        
        # collect 1s from ( x XOR y ) from LSB to MSB
        
        hamming_dist = 0
        for i in range(32):
            
            hamming_dist += (x&1) ^ (y&1)
            
            # both x and y right shift one bit
            x = x >> 1
            y = y >> 1
            
        return hamming_dist



# n : value of max(x, y) 

## Time Complexity: O( 1 )
#
# The overhead in time is the loop iterating on i, which is of O( 32 ) = O( 1 ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and xor variable, which is of O( 1 )



def test_bench():

    test_data = [(1,4), (2,7), (31,15), (127, 86)]


    # expected output:
    '''
    2
    2
    1
    3
    '''

    for test_pair in test_data :

        print( Solution().hammingDistance(*test_pair) )

    return 



if __name__ == '__main__':

    test_bench()