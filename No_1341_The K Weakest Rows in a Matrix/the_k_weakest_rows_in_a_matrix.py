'''

Description:

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]



Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]
 

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

'''



from typing import List
from operator import itemgetter
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
                
        strength = []
        
        # build list of strength from number of solder and row index.
        for i,row in enumerate(mat):
            
            strength.append( (row.count(1), i) )
        
        print( strength )
        
        # sort strength in ascending order by
        # 1. number of soldier
        # 2. row index
        strength.sort(key = itemgetter(0,1) )

        print( strength )
        
        # get the first k items's row index
        result = list( map( itemgetter(1), strength[:k] ) )
        
        return result



# n : the dimension of rows of input matrix, max.
# s : the value of input k

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of sorting, which is O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for strength, which is of O(n), 
# and result, which is if of O(s).
# It takes O( n + s ) = O( n ) totally.


def test_bench():

    test_data = [
                    ([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3),
                    #([[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], 2)
                ]
    

    # expected output:
    '''
    [2, 0, 3]
    [0, 2]
    '''

    for matrix, k in test_data:

        print( Solution().kWeakestRows(mat=matrix, k = k ) )
    
    return



if __name__ == '__main__':

    test_bench()