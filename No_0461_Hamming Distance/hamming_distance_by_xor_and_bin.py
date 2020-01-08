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
        
        # count the 1s in bitstring of ( x XOR y )
        
        return bin(x^y).count('1')
        

        
# n : value of max(x, y) 

## Time Complexity: O( 1 )
#
# The overhead in time is the '{0:{fill}32b}' bit string conversion and str.count('1'), which is of O( 32 ) = O( 1 ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for bit string, which is of O( 1 )



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