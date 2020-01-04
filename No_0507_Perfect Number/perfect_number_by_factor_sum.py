'''

Description:

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)

'''


from math import floor

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 1:
            # corner case
            return False
        
        
        sum_of_factor = 1
        
        for i in range(2, floor( num**0.5 ) + 1 ):
            
            
            if num % i == 0:
                
                if i == num // i :
                    # square root, should only add once
                    sum_of_factor +=  i
                    
                else:
                    # add factor i and (num // i)
                    sum_of_factor += ( i + num // i )
                    
        
        return sum_of_factor == num



# n : the number of input value

## Time Complexity: O( sqrt(n) )
#
# The major overhead in time is the for loop iterating on i, which is of O( sqrt(n) )

## Space Complexity: O( 1 )
#
# The major overhead in space is the storage for math computation, which is of O( 1 )



def test_bench():

    test_data = [ 1, 2, 6, 28, 496, 8128, 33550336, 99999999 ]

    # expected output:
    '''
    False
    False
    True
    True
    True
    True
    True
    False
    '''

    for n in test_data :

        print( Solution().checkPerfectNumber(n) )

    return 



if __name__ == '__main__':

    test_bench()