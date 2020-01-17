'''

Description:

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

'''



from typing import List
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        
        size = len(A)
        
        # a list to store the occurrence of congruence of 0, 1, 2, ..., (K-1)
        modulo_occurrence = [0] * K 
        
        prefix_sum = 0
        for i,number in enumerate(A):
            
            # accumulate the prefix summation, where prefix begins from index 0
            prefix_sum += number
            
            # compute remainder number of prefix_sum % k
            # because there is chance to have negative value, mod twice to get positive remainder
            modulo_k = ( (prefix_sum % K + K) %K )
            
            # accumulate the occurrence of remainder of mod K
            modulo_occurrence[modulo_k] += 1
        
        
        number_of_subarr_sum_div_by_k = 0
        for remainder in range(K):
            
            number_of_same_remainder = modulo_occurrence[remainder]
            
            # If there are at least two index i, j, i =\= j, 
            # such that prefix sum_i and prefix sum_j with the same remainder of mod K,
            # then the number of subarray sum divisible by K = C(n, 2) = [ n * (n-1) ] / 2
            # where n = the number of the same remainer
            if number_of_same_remainder > 1 :
                number_of_subarr_sum_div_by_k += number_of_same_remainder*(number_of_same_remainder-1)//2
        
        # plus the subarry sum with multiple 5, where subarray begin from index 0
        number_of_subarr_sum_div_by_k +=  modulo_occurrence[ 0 ]
        
        return number_of_subarr_sum_div_by_k



# n : the length of input list, A.
# k : the input value of K.

## Time Complexity: O( n + k )
#
# The overhead in time is the loops, one is of O(n), the other is of O(k).
# It takes O( n + k ) in total.


## Space Complexity: O( k )
#
# The overhead in space is the storage for list, modulo_occurrence, which si of O( k ).



def test_bench():

    test_data = [
                    ([4,5,0,-2,-3,1], 5),
                    ([4,5,0,-2,-3,1], 3)
                ]

    # expected output:
    '''
    7
    6
    '''

    for sequence, k in test_data:

        print( Solution().subarraysDivByK( sequence, k ) )
    

    return 



if __name__ == '__main__':

    test_bench()

