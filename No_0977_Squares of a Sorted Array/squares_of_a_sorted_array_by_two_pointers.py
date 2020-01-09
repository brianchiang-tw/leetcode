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
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        size = len(A)
        
        square_list = [0] * size
        
        left, right = 0, size-1
        
        write_idx = size-1
        
        while write_idx >= 0:
            
            left_val, right_val = A[left], A[right]
            
            if abs(A[left]) >= abs(A[right]) :
                
                square_list[write_idx] = left_val*left_val
                left += 1
            
            else:
                
                square_list[write_idx] = right_val*right_val
                right -= 1
                
                
            write_idx -= 1
            
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