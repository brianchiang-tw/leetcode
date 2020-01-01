'''

Description:

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''


from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        pascal_tri = []
        
        for i in range( numRows ):
            
            if i == 0:
                pascal_tri.append( [1] )
                continue
                
            cur_row = [ 1 ] * (i+1)
            
            
            for j in range( len(cur_row) ):
                
                if j != 0 and j != i:
                    cur_row[j] = pascal_tri[i-1][j-1] + pascal_tri[i-1][j]
                    
            pascal_tri.append( cur_row )
            
        return pascal_tri


# n : the input value of numRows

## Time Complexity: O( n^2 )
#
# The major overhead in time is the double for loops iterating on i and j, which is of O( n^2 )

## Space Complexity: O( n^2 )
#
# The major overhead in time is the storage for pascal triangle elements, which is of O( n^ 2)



def test_bench():

    test_data = [1,2,3,4,5]


    # expected output:
    '''
    [[1]]
    [[1], [1, 1]]
    [[1], [1, 1], [1, 2, 1]]
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    '''

    for n in test_data:

        pascal_triangle = Solution().generate( n )

        print( pascal_triangle )

    return 



if __name__ == '__main__':

    test_bench()