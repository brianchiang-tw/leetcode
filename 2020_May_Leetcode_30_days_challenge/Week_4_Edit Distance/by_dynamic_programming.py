'''

Description:

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character



Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')



Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    
        # padding one whitespace for empty string representation
        word_1 = ' ' + word1
        word_2 = ' ' + word2
        
        h, w = len(word_1), len(word_2)
        
        min_edit_dist = [ [ 0 for _ in range (w) ] for _ in range(h) ]
        
        # initialization for top row
        for x in range(1, w):
            min_edit_dist[0][x] = x
            
        # initialization for left-most column
        for y in range(1, h):
            min_edit_dist[y][0] = y
            
        # compute minimum edit distance with optimal substructure
        for y in range(1, h):
            for x in range(1, w):
                
                if word_1[y] == word_2[x]:
                    # current character match, no need to edit
                    min_edit_dist[y][x] = min_edit_dist[y-1][x-1]
                else:
                    # current character mismatch, choose the method of lowest cost, among character replacement, character addition, or character delection
                    min_edit_dist[y][x] = min( min_edit_dist[y][x-1], min_edit_dist[y-1][x], min_edit_dist[y-1][x-1]) + 1
        
        return min_edit_dist[-1][-1]



# m : the length of word1
# n : the length of word2

## Time Complexity: O( m*n )
#
# The overhead in time is the cost of nested loop, which is of O( m * n )

## Space Complexity: O( m*n )
#
# The overhead in space is the storage for dynamic programming table, which is of O( m*n )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'word1 word2')

def test_bench():

    test_data = [
                    TestEntry( word1 = "horse", word2 = "ros" ),
                    TestEntry( word1 = "intention", word2 = "execution" ),
                ]

    # expected output:
    '''
    3
    5
    '''

    for t in test_data:
        print( Solution().minDistance( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()