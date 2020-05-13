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
   Hide Hint #1  
To reach nth step, what could have been your previous steps? (Think about the step sizes)

'''



class Solution:
    
    def __init__(self):
        
        self.cache = {}
    
    def climbStairs(self, n: int) -> int:    
        
        if n in self.cache:
            return self.cache[n]
        
        if n == 0 or n == 1:
            return 1
        
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.cache[n] = result
            return result



# n : the input value

## Time Complexity: O( n )
#
# The overhead in time is the cost of recursion depth, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for table, cache, which is of O( n )



def test_bench():

    test_data = [
                    0,1,2,3,4,5,6,7,8,9,10,30
                ]

    # expected output:
    '''
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    1346269
    '''

    for t in test_data:

        print( Solution().climbStairs( n = t) )

    return



if __name__ == '__main__':

    test_bench()