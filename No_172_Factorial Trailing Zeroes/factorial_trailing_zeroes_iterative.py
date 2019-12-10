'''

Description:

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

'''

# Hint:
# Trailing 0s are generated from the product of 5 x 2 pair.
# And the bounding condition is 5 instead of 2 ( multiplier of 5 is less than multiplier of 2 within constant n! )
#
# Find the 5 x 2 pair can be reduced to find the number of factor 5 in n!

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        count_of_5 = 0
        
        while n > 4 :
            
            count_of_5 += int( n // 5 )
            n = n / 5
        
        return count_of_5



# N : the input number of n

## Time Complexity: O( log n )
#
# The overhead is the while loop, it takes O( log5 n ) to reach base case.

## Space Complexity: O( 1 )
# 
# The overhead is the variable for looping index and counter of 5 


def test_bench():

    test_data = [3, 5]
    
    # expected output:
    '''
    0
    1

    Note:
    3 ! = 6, no trailing 0s

    5 ! = 120, with 1 trailing 0
    '''

    for n in test_data:

        print( Solution().trailingZeroes(n) )


    return


if __name__ == '__main__':

    test_bench()