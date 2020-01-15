'''

Description:

In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

'''



from typing import List
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        ori_rows, ori_cols = len(nums), len(nums[0])
        
        if ori_rows * ori_cols != r * c or (ori_rows, ori_cols) == (r, c):
            # Quick response:
            # 
            # mismatch of total number of elements
            # or
            # dimension is the same as original
            
            return nums
        
        else:
            
            # flatten nums to 1D array
            flatten_array = [ element for rows in nums for element in rows ]
            
            # construct  reshape_arr by list comprehension
            reshape_arr = [ flatten_array[ y*c : y*c+c ] for y in range(r) ]
            
            return reshape_arr



# m , n : dimension of rows and columns of input matrix, nums.

## Time Complexity: O( m * n )
#
# The overhead in time is the flattening and list comprehension, which are of O( m * n )

## Space Comeplxity: O( m * n )
#
# The overhead in space is the storage for reshpaed matrix, which is of O( m * n )



def test_bench():

    test_data = [
                    ([[1,2],[3,4]], 1, 4),
                    ([[1,2],[3,4]], 2, 4),
                    ([[1,2],[3,4]], 2, 2),
                    ([[1,2],[3,4]], 4, 1)
                ]
    

    # expected output:
    '''
    [[1, 2, 3, 4]]
    [[1, 2], [3, 4]]
    [[1, 2], [3, 4]]
    [[1], [2], [3], [4]]
    '''

    for matrix, r, c in test_data:

        print( Solution().matrixReshape(matrix, r, c) )

    return 



if __name__ == '__main__':

    test_bench()