'''

Description:

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''


class Solution:
    def climbStairs(self, n: int) -> int:

        
        # base case:
        # f(0) = 1
        # f(1) = 1    
        ways_to_climb = [ 1, 1 ] + [ 0 ] * ( n-1 )
        
        
        # recurrence:
        # ways to reach level n 
        # = ways to reach level (n-1) + ways to reach level (n-2)
        #
        # f(n) = f(n-1) + f(n-2)
        
        for i in range(2, n+1):
            ways_to_climb[i] = ways_to_climb[i-1] + ways_to_climb[i-2]
        
        return ways_to_climb[n]



# n : the number of input value

## Time Compleixty: O( n )
#
# The major overhead in time is the for loop iterating on i, which is of O( n ).

## Space Complexity: O( n )
#
# The major overhead in space is the storage for array ways_to_climb, which is of O( n ).


def test_bench():

    test_data = [ 1, 2, 3, 4, 5, 10 ]

    for n in test_data:

        print( Solution().climbStairs(n) )

    return 



if __name__ == '__main__':

    test_bench()
        