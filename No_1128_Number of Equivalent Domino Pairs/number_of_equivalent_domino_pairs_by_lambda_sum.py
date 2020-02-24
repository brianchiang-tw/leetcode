'''

Description:

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

'''


from collections import defaultdict
from typing import List
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        pair_occ = defaultdict( int )
        
        counter_of_qeuivalent = 0
        
        for domino in dominoes:
            pair = ( min(domino[0],domino[1]), max(domino[0], domino[1]) )    
            pair_occ[ pair ] += 1
        
        
        
        eq_occ = lambda x: x*(x-1) // 2
        return sum( map( eq_occ, pair_occ.values() ) ) 


        
# n : the length of input dominoes

## Time Complexity: O( n )
#
# The overhead in time is the loop, iterating on dominoes, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping variable, which is of O( 1 )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'dominoes')
def test_bench():

    test_data = [
                    TestEntry( dominoes = [[1,2],[2,1],[3,4],[5,6]] ),
                    TestEntry( dominoes = [[1,2],[2,1],[3,4],[5,6],[1,2]] ),
                    TestEntry( dominoes = [[1,2],[6,5],[3,4],[5,6],[1,2]] ),    
                ]
    
    # expected output:
    '''
    1
    3
    2
    '''

    for t in test_data:

        print( Solution().numEquivDominoPairs(t.dominoes) )
    
    return 



if __name__ == '__main__':

    test_bench()