'''

Description:

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

 

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1



Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false



Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Note:

3 <= A.length <= 50000
-10000 <= A[i] <= 10000


'''



from typing import List
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        
        
        sum_of_A = sum(A)
        
        if sum_of_A % 3 != 0:
            
            return False
        
        else:
            target = sum_of_A // 3

            size = len(A)
            accumulation, partition = 0, 0

            for idx,number in enumerate(A):

                accumulation += number
                
                if partition == 0:
                    if accumulation == target:
                        # We find first chunk of 1/3
                        partition = 1
                        
                        
                elif partition == 1:
                    if accumulation == 2*target and idx != (size-1):
                        # We find second chunk of 1/3 in the middle
                        # then the last chink must be 1/3 also.
                        
                        # Therefore, we have 3 chunks of 1/3
                        partition = 3
                        return True
                

            return False



# n : the length of input array, A

## Time Complexity: O( n )
#
# The overhead in time is the cost of sum( A ) and the loop, iterating on A, which are of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable and accumulation, which is of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1 ] ),
                    TestEntry( sequence = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1 ] ),
                    TestEntry( sequence = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4 ] ),
                    TestEntry( sequence = [1, -1 , 1, -1 ]),
                ]

    # expected output:
    '''
    True
    False
    True
    False
    '''


    for t in test_data:

        print( Solution().canThreePartsEqualSum( A = t.sequence ) )
    
    return



if __name__ == '__main__':

    test_bench()
