'''

Description:

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''



class Solution:
    
    def sieve_algorithm(self, n: int)-> bool:
        
        if n <= 2:
            return 0
        
        
        is_prime = [ True for _ in range(n) ]
        
        # Base case handle
        is_prime[0] = False
        is_prime[1] = False
        
        upper_bound = int(n ** 0.5)
        for i in range( 2, upper_bound+1 ):
            
            if not is_prime[i]:
                # only run on prime number
                continue
            
            
            for j in range( i*i, n, i):
                # remove all multiples of i
                is_prime[j] = False
                
        return sum(is_prime)
    
    
    
    def countPrimes(self, n: int) -> int:
        
        return self.sieve_algorithm(n)



# n : the input value

## Time Complexity: O( n loglog n )
#
# The overhead in time is the cost of Sieve of Eratosthenes algorithm, which is of O( n loglog n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for lookup table, is_prime, which is of O( n ).


def test_bench():

    test_data = [ 10, 20, 100, 1000, 2000, 5000, 10000]

    # expected output:
    '''
    4
    8
    25
    168
    303
    669
    1229    
    '''

    for n in test_data:

        print( Solution().countPrimes(n) )
    
    return 



if __name__ == '__main__':

    test_bench()