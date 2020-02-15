'''

Description:

Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.



Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100

'''



from math import factorial
from math import sqrt
class Solution:
    
    def judge_prime( self, k:int) -> bool:
        '''
        Input: positive integer
        Output: True for prime number. Otherwise, retunr False
        '''

        if k == 1:
            return False
        
        if k == 2:
            return True
        
        for i in range(2, int( sqrt(k)+1 ) ):
            
            if k % i == 0:
                return False
            
        return True
    
    
    
    def numPrimeArrangements(self, n: int) -> int:
        '''
        Input: n
        Output: Prime arrangements for n
        '''
        
        
        # modulo constant defined by description
        mod_constant = int(1e9)+7
        
        counter_of_prime = 0
        
        # check positive integer from 1 to n
        for i in range(1,n+1):
            
            if self.judge_prime(i):
                counter_of_prime += 1
        
        # Let q as counter_of_prime
        # then all permutation
        # = ( q! * ( n-q)! ) mod (10^9 + 7)
        all_permutation = ( factorial(counter_of_prime) * factorial(n-counter_of_prime) ) % mod_constant
        
        return all_permutation



# n : the value of input integer.

## Time Complexity: O( n*sqrt(n) )
#
# The overhead in time is the for loop, which is of O( n ),
# and the cost of helper function, judge_prime, which is of O( sqrt(n) )
# 
# It takes O( n * sqrt(n) ) in total


## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index nad arithmetic computation, which is of O( n ).

def test_bench():

    test_data = [
                    5,
                    10,
                    36,
                    100
                ]

    # expected output:
    '''
    12
    17280
    462170018
    682289015
    '''

    for n in test_data:
        
        print( Solution().numPrimeArrangements(n) )
    
    return



if __name__ == '__main__':

    test_bench()