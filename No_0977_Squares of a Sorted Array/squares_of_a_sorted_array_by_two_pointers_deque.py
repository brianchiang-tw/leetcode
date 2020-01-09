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



from collections import deque
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        size = len(A)
        
        # output 
        square_list = deque()
        
        left, right = 0, size-1
        
        write_idx = size-1
        
        # left start from left hand side ( negative side )
        # right start from right hand side ( positive side )
        while left <= right:
            
            left_val, right_val = A[left], A[right]
            
            # compare absolute value, choose the bigger one, then append from tail to head
            if abs(A[left]) >= abs(A[right]) :
                
                square_list.appendleft( left_val*left_val )
                left += 1
            
            else:
                
                square_list.appendleft( right_val*right_val )
                right -= 1
                
        return square_list



# n : the length of input list, A.

## Time Complexity : O( n )
#
# The overhead in time is the linear traverse of two-pointers, which is of O( n ).

## Space Complexity : O( n )
#
# The overhead in space is the storage for the square_list, which is of O( n ).



def test_bench():

    test_data = [
                    [-4,-1,0,3,10],
                    [-7,-3,2,3,11]
                ]

    # expected output:
    '''
    [0, 1, 9, 16, 100]
    [4, 9, 9, 49, 121]
    '''



    for sequence in test_data :

        print( list( Solution().sortedSquares(sequence) ) )
    
    return 



if __name__ == '__main__':

    test_bench()