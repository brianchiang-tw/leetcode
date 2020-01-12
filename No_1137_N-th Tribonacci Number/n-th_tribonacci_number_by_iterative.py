'''

Description:

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


'''



class Solution:
    
    def tribonacci(self, n: int) -> int:
        
        t0, t1, t2 = 0, 1, 1
        
        # base case:
        if n == 0 :
            return t0
        
        # base case:
        if n == 1 or n == 2:
            return t1
        
        # general case:
        for i in range(3, n+1):
            
            t_n = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = t_n
            
        return t_n



# n : the input value

## Time Compexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for base case and looping variable, which is of O( 1 )


def test_bench():

    test_data = [0, 1, 2, 3, 4, 5, 6, 10, 20, 25]

    # expected output:
    '''
    0
    1
    1
    2
    4
    7
    13
    149
    66012
    1389537
    '''

    for n in test_data:

        print( Solution().tribonacci(n) )

    return 



if __name__ == '__main__':

    test_bench() 