''''

Description:

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9

'''


import collections
class Solution(object):

    def shortestSubarray( self, A, K):
        
        # get the length of input list A
        size = len(A)

        # sub_sum denotes as S
        sub_sum = [ 0 ]

        # update sub_sum
        # S[ 0 ] initialized to 0
        # S[ 1 ] = A[ 0 ]
        # S[ 2 ] = A[ 0 ] + A[ 1 ]
        # S[ 3 ] = A[ 0 ] + A[ 1 ] + A[ 2 ]
        # ...
        # S[ i ] = A[ 0 ] + A[ 1 ] + A[ 2 ] + ... + A[ i-1 ]
        for element in A:
            sub_sum.append( sub_sum[-1] + element )

        # Create a double-ended queue, named queue, to store index of S
        queue = collections.deque()    

        # a variable to store shortest subarray range length
        range_length = ( size + 1 )


        # check each S[ i ], i iterates from 0 to size
        for i in range(size+1):

            # If queue is not empty, compare S[ i ] and S[ last_of_quque ]
            # If S[ i ] < S[ last_of_queue], keep removing last element of queue
            while queue and sub_sum[i] <= sub_sum[ queue[-1] ]:
                queue.pop()

            # If queue is non empty, compare S[ i ] and S[ first_of_queue ]
            # If S[ i ] - S[ first_of_queue ], then we collect one subarray with sum >= k
            # update range_length = min( previous range length, i - first_of_quque )
            while queue and ( sub_sum[i] - sub_sum[ queue[0] ] ) >= K:
                range_length = min( range_length, i - queue.popleft() )


            # push i on the right end of queue
            queue.append( i )

        # if range_length < size+1, return range length
        # otherwise, return -1 (no valid solution)
        return range_length if range_length < (size + 1) else -1 



# N : the length of input list A

## Time Complexity: O( N )
#
# The workhorse is the for loop to scan S[i] with O( N )
# Although there are two while inside, their complexity is much smaller than O(N), 
# because the total count of while loop iteration apporach constant.

## Space Complexity: O( N )
# The overhead is sub_sum to maintain a dynamic programming array S[i] = sum( A[0] ... A[i-1] ) with O( N )
# Another minor loading is queue, to maintain several contigious index of S, far less than O( N )


def test_bench():

    test_data = [ 
                    ( [1], 1 ),
                    ( [1, 2], 4),
                    ( [2, -1, 2], 3)    
                ]

    # expected output:
    '''
    1
    -1
    3
    '''


    for test in test_data :

        length_of_subarry = Solution().shortestSubarray( test[0], test[1] )

        print( length_of_subarry )

    

    return



if __name__ == '__main__':

    test_bench()
