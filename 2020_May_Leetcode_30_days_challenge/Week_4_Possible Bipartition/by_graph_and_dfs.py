'''

Description:

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]



Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false



Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].

'''



from typing import List
from collections import defaultdict

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        # Constant defined for color drawing to person
        NOT_COLORED, BLUE, GREEN = 0, 1, -1
        
        # -------------------------------------
        
        def helper( person_id, color ):
            
            # Draw person_id as color
            color_table[person_id] = color
            
            # Draw the_other, with opposite color, in dislike table of current person_id
            for the_other in dislike_table[ person_id ]:
   
                if color_table[the_other] == color:
                    # the_other has the same color of current person_id
                    # Reject due to breaking the relationship of dislike
                    return False

                if color_table[the_other] == NOT_COLORED and (not helper( the_other, -color)):
                    # other people can not be colored and keeping dis-like relationship
                    return False
                    
            return True
        
        
        # ------------------------------------------------
        if N == 1 or not dislikes:
            # Quick response for simple cases
            return True
        
        
        
        # each person maintain a list of dislike
        dislike_table = defaultdict( list )
        
        # cell_#0 is dummy just for the convenience of indexing from 1 to N
        color_table = [ NOT_COLORED for _ in range(N+1) ]
        
        for p1, p2 in dislikes:
            
            # P1 and P2 dislike each other
            dislike_table[p1].append( p2 )
            dislike_table[p2].append( p1 )
            
        
        # Try to draw dislike pair with different colors in DFS
        for person_id in range(1, N+1):
            
            if color_table[person_id] == NOT_COLORED and (not helper( person_id, BLUE)):
                
                return False 
        
        return True



# V : total number of nodes, i.e., the value of N
# E : total number of edges, i.e., the length of dislikes

## Time Complexity: O( V + E )
#
# The overhead in time is the cost of DFS, which is of O( V + E )

## Space Complexity: O( V + E )
#
# The overhead in space is the storage for recursion stack, which is of O( V + E )

        
        
from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'N dislikes')

def test_bench():

    test_data = [
                    TestEntry( N = 4, dislikes = [[1,2],[1,3],[2,4]] ),
                    TestEntry( N = 3, dislikes = [[1,2],[1,3],[2,3]] ),
                    TestEntry( N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]] ),
                    TestEntry( N = 4, dislikes = [[1,2],[2,4],[3,4]] ),
                ]

    # expected output:
    '''
    True
    False
    False
    True
    '''

    for t in test_data:
        print( Solution().possibleBipartition( *t ) )


    return



if __name__ == '__main__':

    test_bench()