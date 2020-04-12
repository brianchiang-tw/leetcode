'''

Description:

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000

'''




class Solution:
    def numOfWays(self, n: int) -> int:
        
        # Base case:
        # for n = 1
        # painting( n = 1 ) 
        # = head_tail_equal( n = 1 ) + head_tail_differnt( n = 1 )
        # = 6 + 6
        # = 12
        
        head_tail_equal = 6
        head_tail_differnt = 6
        
        if n == 1:
            # Quick response for base case
            return head_tail_equal + head_tail_differnt
        
        
        # Recurrence for general case:
        # for n >= 2
        
        # painting( n ) = 5 * head_tail_equal(n-1) + 4 * head_tail_differnt(n-1)
        
        # where
        
        # head_tail_equal( n ) = 3 * head_tail_equal(n-1) + 2 * head_tail_differnt(n-1)
        
        # head_tail_differnt( n ) = 2 * head_tail_equal(n-1) + 2 * head_tail_differnt(n-1)
        
        modulo = 10**9 + 7
        
        for i in range(2, n+1):
            
            next_ht_equal = ( 3 * head_tail_equal + 2 * head_tail_differnt ) % modulo
            next_ht_different = ( 2 * head_tail_equal + 2 * head_tail_differnt ) % modulo
            
            head_tail_equal, head_tail_differnt = next_ht_equal, next_ht_different

            
        ways_to_paint = head_tail_equal + head_tail_differnt
        
        return (ways_to_paint % modulo)



# n : the value of input

## Time Complexity: O( n )
#
# The overhead in time is the cost of for loop, which is of O( n ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for looping index and temporary variable for computation, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntrry', 'n')
def test_bench():

    test_data = [
                    TestEntry( n = 1 ),
                    TestEntry( n = 2 ),
                    TestEntry( n = 3 ),
                    TestEntry( n = 7 ),
                    TestEntry( n = 5000 ),
                ]        

    # expected output:
    '''
    12
    54
    246
    106494
    30228214
    '''


    for t in test_data:

        print( Solution().numOfWays( n = t.n ) )

    return



if __name__ == '__main__':

    test_bench()