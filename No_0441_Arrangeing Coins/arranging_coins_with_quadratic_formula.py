'''

Description:

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

'''


from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:

        #quick response
        if n <= 1:
            return n
                
        #solve k(k+1)/2 <= n , keep k as large as possible
        k = int( (-1 + sqrt( 1 + 8*n )) / 2 )
        
        return k


# N : the input value of n

## Time Complexity : O( 1 )
#
# The overhead is the computation of quardatic equation of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead is the variable for n, k with fixed size


def test_bench():

    test_data = list( range(6, 12) )

    # expected output
    '''
    3
    3
    3
    3
    4
    4

    Note:
    stair case of level 3 = 3 * 4 / 2 = 6
    stair case of level 4 = 4 * 5 / 2 = 10
    '''

    for n in test_data:

        print( Solution().arrangeCoins(n) )


    return 


if __name__ == '__main__':

    test_bench()