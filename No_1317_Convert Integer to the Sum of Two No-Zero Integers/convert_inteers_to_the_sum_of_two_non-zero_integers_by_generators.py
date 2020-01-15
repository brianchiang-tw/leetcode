'''

Description:

Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.
Example 2:

Input: n = 11
Output: [2,9]
Example 3:

Input: n = 10000
Output: [1,9999]
Example 4:

Input: n = 69
Output: [1,68]
Example 5:

Input: n = 1010
Output: [11,999]
 

Constraints:

2 <= n <= 10^4

'''



class Solution:
    def getNoZeroIntegers(self, n):
        return next([a, n-a] for a in range(n) if '0' not in f'{a}{n-a}')   


# n : the input value

## Time Complexity: O( n log n )
#
# There are n possible enumerated integers, each integer has logn bit to check if it has 0 or not.
# It takes O( n log n ) in total.

## Space Complexity: O( 1 )
#
# The overhead in space is the variable for enumerated integer output and math computation, which is of O( 1 ). 


def test_bench():

    test_data = [2, 11, 69, 10000, 1010, 101, 99]

    # referernce output: ( it may change every time due to randomness)
    '''
    [1, 1]
    [4, 7]
    [2, 67]
    [8386, 1614]
    [423, 587]
    [94, 7]
    [42, 57]    
    '''


    for number in test_data:

        print( Solution().getNoZeroIntegers(number) )
    
    return 



if __name__ == '__main__':

    test_bench()