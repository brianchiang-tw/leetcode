'''

Description:

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true

'''


from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        size = len(A)
        
        # check if A follows the definition of mountain
        if size < 3:
            return False
        
        # go uphill
        for i in range( 1, size ):
            
            if A[i] > A[i-1]:
                continue
                
            elif A[ i ] == A[ i-1 ]:
                # flat plain is found, break the definition of mountain
                return False
            
            else:
                if i == 1:
                    # direct go down, break the definition of mountain
                    return False
                else:
                    break
                
        
        # go downhill
        for j in range( i, size):
            
            if A[j] < A[j-1]:
                continue
            else:
                # valley is found, break the definition of mountain
                return False
        else:
            
            # mountain traverse is completed
            return True



# n :the length of input array A:

## Time Complexity : O( n )
#
# Linear probing for array A, it takes O( n ) to traverse.

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable and index, which is of O( 1 ).


def test_bench():

    test_data = [
                    [2,1],
                    [3,5,5],
                    [0,3,2,1],
                    [5],
                    [100,2],
                    [2, 100],
                    [100,2,100],
                    [2,100,50]
                ]


    # expected output:
    '''
    False
    False
    True
    False
    False
    False
    False
    True
    '''

    for height_curve in test_data:

        print( Solution().validMountainArray(height_curve) )

    return 



if __name__ == '__main__':

    test_bench()
