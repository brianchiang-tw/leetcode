'''

Description:

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

 

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])



Example 2:

Input: [4,8,12,16]
Output: 2



Example 3:

Input: [100]
Output: 1
 

Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9

'''



from typing import List
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        
        
        size = len(A)
        
        if size == 1:
            return 1
        
        cur_turbu_length = 1 + ( A[0] != A[1] )
        
        max_length = cur_turbu_length
        
        prev_diff = A[1] - A[0]
        
        for i in range(1, size-1):
            post_diff = A[i+1] - A[i]
            
            if prev_diff*post_diff < 0:
                # turbulent subarray can extend from previous element to next element
                cur_turbu_length += 1
                
                max_length = max( max_length, cur_turbu_length )
            
            else:
                # turbulent subarray restarts here
                cur_turbu_length = 1 + (post_diff != 0)
            
            # update pre_diff
            prev_diff = post_diff
            
        return max_length



# n : the length of input array, A

## Time Complexity: O( n )
#
# The overhead in time is the for loop, iterating on A, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and variable for optimization computation, which is of O( 1 ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')
def test_bench():

    test_data = [
                    TestEntry( sequence = [9,4,2,10,7,8,8,1,9] ),
                    TestEntry( sequence = [4,8,12,16] ),
                    TestEntry( sequence = [100] ),
                    TestEntry( sequence = [10,1,5,3,6,6] ),
                ]

    # expected output:
    '''
    5
    2
    1
    5
    '''

    for t in test_data:

        print( Solution().maxTurbulenceSize( A = t.sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()