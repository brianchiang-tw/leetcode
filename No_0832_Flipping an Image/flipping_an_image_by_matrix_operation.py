'''

Description:

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1

'''


from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in range( len(A) ):
            
            for j in range( len(A[i])//2  ):
                # flip image horizontally
                A[i][j], A[i][-j-1] = A[i][-j-1], A[i][j]
            
            for j in range( len(A[i]) ):
                # invert image, toogle 0/1
                A[i][j] = A[i][j]^1

        
        return A



# m, n : the dimension of rows and columns

## Time Complexity: O( m * n )
#
# The overhead in time is the nested for loops iterating on (i, j), which are of O( m * n )

## Space Complexity: O( 1 )
#
# The overhead in time is the vaariable for matrix operation, which is of O( 1 ).



def test_bench():

    test_data = [
                    [[1,1,0],[1,0,1],[0,0,0]],
                    [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
                ]

    # expected output:
    '''
    [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
    [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    '''


    for test_image in test_data:

        print( Solution().flipAndInvertImage(test_image) )
    
    return 



if __name__ == '__main__':

    test_bench()