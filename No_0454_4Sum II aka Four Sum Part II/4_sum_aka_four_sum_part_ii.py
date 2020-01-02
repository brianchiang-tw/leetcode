'''
Description:
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output:
2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''


# allow python featre, type hints
from typing import List

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
      
                
        # Key concept:
        # This time, what we need is the count of valid four sum, instead of index
        
        # Again, it is nice to take advantage of 2-sum, 
        # by using hash(python dictionay) and the trick of dual = target - x
        
        
        value_hash = dict()
        
        for a in A:
            for b in B:
                
                two_sum = a + b
                
                # update the method count of two_sum in terms of hashing
                # key: value
                # value: total count of pair where pair sum = value
                value_hash[ two_sum ] = value_hash.get( two_sum, 0) + 1
        
        
        
        count_of_zero_4_sum = 0
                
        for c in C:
            for d in D:
                
                dual = 0 - c - d
                
                # accumulate the count of four sum where four sum = 0
                count_of_zero_4_sum += value_hash.get( dual, 0)
        
        
        return count_of_zero_4_sum


## Time Complexity
# O( N^2 )

# Preprocess of sorting input list takes O( N log N )

# Outer for loop takes O( N ) to iterate index a
# Also, inner while loop takes O( N ) to iterate index b
# These two loops takes O( N^2 )

# Similarly, next two loops for c, d takes O( N^2 )

## Space Complexity
# O( 1 )

# In the nested loop, we use variables for index a, b, two_sum, c, d, as well as dual
# and a list to store the solution
# These usage are of O( 1 )




def test_bench():

    test_data =  ( [ 1, 2], [-2,-1], [-1, 2], [ 0, 2] )
    
    count_of_four_sum = Solution().fourSumCount(  A = test_data[0], B = test_data[1], C = test_data[2], D = test_data[3] )

    print( count_of_four_sum )
    # expected output:
    '''
    2
    '''


    return


if __name__ == '__main__':

    test_bench()