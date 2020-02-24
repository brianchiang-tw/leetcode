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
        
        pair_occ = defaultdict(int)
        
        counter_of_equivalent = 0
        
        for domino in dominoes:
            
            # hash key_id for domino
            # domino (a, b) = domino (b, a)
            key_id = 10 * domino[0] + domino[1] if domino[0] < domino[1] else 10 * domino[1] + domino[0]
            
            # accumulate the number of equivalnet dominos when looking back
            counter_of_equivalent += pair_occ[ key_id ]
            
            # update occurrence of current key_id
            pair_occ[ key_id ] += 1
        
        return counter_of_equivalent
        


# n : the length of input dominoes

## Time Complexity: O( n )
#
# The overhead in time is the loop, iterating on dominoes, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, pair_occ, which is of O( n )



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