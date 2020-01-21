'''

Description:

ou have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]



Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]



Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.

'''



from typing import List
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        
        # adj list for gardens
        adjacenct_list = [ [] for i in range(N) ]
        
        # record of flower type to each garden
        # 0 : not planted yet
        # 1~4: corresponding flower type
        flower_type_garden = [ 0 for i in range(N) ]
        
        
        for p in paths:
            
            # get nodes of path
            garden_a, garden_b = p
            
            # path is un-directed
            # convert path to corresponding linkage in adjacency list
            adjacenct_list[ garden_a-1].append( garden_b-1 )
            adjacenct_list[ garden_b-1].append( garden_a-1 )
        
        
        # assign flower type to each garden
        for garden in range(N):
            
            neighbor_flower_type = []
            
            # collect flower type of neighborhood
            for neighbor in adjacenct_list[garden]:    
                neighbor_flower_type.append( flower_type_garden[neighbor] )

            # flower types are denoted 1, 2, 3, 4
            for flower_type in range(1,5):
                
                # avoid repetition with neighbor's flower type
                if flower_type in neighbor_flower_type:
                    continue
                    
                else:    
                    flower_type_garden[garden] = flower_type
                    break
                
        return flower_type_garden
                


# n : the number of gardens

## Time Complexity: O( n )
#
# The overhead in time is the outer loop iterating on garden, which is of O( n )
# Note that the for loop iterating on neighbor is of O( 3 ), 
# and the for loop iterating on flower_type is of O( 4 ).


## Space Complexity: O( n )
#
# The overhead in space is the storage adjacenct_list as well as flower_type_garden, which is of O( n )



def test_bench():
    
    test_data = [
                    (3, [[1,2],[2,3],[3,1]]),
                    (4, [[1,2],[3,4]]),
                    (4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])
                ]

    # expected output:
    '''
    [1, 2, 3]
    [1, 2, 1, 2]
    [1, 2, 3, 4]    
    '''


    for n, list_of_path in test_data:

        print( Solution().gardenNoAdj(n,list_of_path) )

    return



if __name__ == '__main__':

    test_bench()
                
            
            