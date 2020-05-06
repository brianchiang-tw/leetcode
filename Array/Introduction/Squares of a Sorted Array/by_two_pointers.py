'''

Description:

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]



Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

'''


from typing import List

from collections import deque

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        left, right = 0, len(A)-1
        
        output = deque()

        while left <= right:
            
            # Choose the maximal one, append on the left hand side of queue
            if abs( A[left] ) >= abs( A[right] ):
                output.appendleft( A[left]**2 )
                left += 1
                
            else:
                output.appendleft( A[right]**2 )
                right -= 1
                
        return [ *output ]



# n : the length of input list, A

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence= [-4,-1,0,3,10] ),
                    TestEntry( sequence= [-7,-3,2,3,11] ),
                ]        

    # expected output:
    '''
    [0, 1, 9, 16, 100]
    [4, 9, 9, 49, 121]
    '''

    for t in test_data:

        print( Solution().sortedSquares( A = t.sequence) )

    return                



if __name__ == '__main__':

    test_bench()