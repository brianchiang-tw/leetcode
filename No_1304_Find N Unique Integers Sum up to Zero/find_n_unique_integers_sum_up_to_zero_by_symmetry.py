'''

Description:

Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000

'''


from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        # generate those numbers in symmetry
        zero_sum_arr = list( range( -(n//2), n//2 + 1, 1 ) )
        
        if n%2 == 0:
            zero_sum_arr.remove( 0 )
        
        return zero_sum_arr



# n : the value of input number

## Time Complexity: O( n )
#
# The overhead in time is the list( range( ... ) ) operation, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is storage for output, zero_sum_arr, which is of O( n ).





def test_bench():

    test_data = [20,5,4,3,2,1]

    # expected output:
    '''
    [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [-2, -1, 0, 1, 2]
    [-2, -1, 1, 2]
    [-1, 0, 1]
    [-1, 1]
    [0]
    '''


    for n in test_data:

        print( Solution().sumZero(n) )

    return 



if __name__ == '__main__':

    test_bench()