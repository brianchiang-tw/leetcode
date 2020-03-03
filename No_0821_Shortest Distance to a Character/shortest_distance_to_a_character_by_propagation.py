'''

Description:

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

'''


from typing import List

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        
        shortest_dist = []
        size = len(S)
        
        if size == 1:
            # Quick response for single character test case
            # Description guarantee that character C must exist in string S
            return [0]
        
        
        # Propagate distance from left to right
        for idx, char in enumerate(S):
            
            if char == C:
                shortest_dist.append(0)
            else:
                if idx == 0:
                    shortest_dist.append( size )
                else:
                    # Propagate distance from C on left hand side
                    shortest_dist.append( shortest_dist[-1] + 1)
                
                
                
        # Propagate distance from right to let               
        for idx in range(2, size+1):
            
            # Propagate distance from C on right hand side
            shortest_dist[-idx] = min(shortest_dist[-idx], shortest_dist[-idx+1]+1 )

                
        return shortest_dist



# n : the charachter length of input string, S.

## Time Complexity: O( n )
#
# The overhead in time is the for loops, iterating on S, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for table, shortest_dist, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string character')
def test_bench():

    test_data = [
                    TestEntry(string = 'loveleetcode', character = 'e'),
                    TestEntry(string = 'loveleetcode', character = 'o'),
                    TestEntry(string = 'loveleetcode', character = 'l'),
                ]

    # expected output:
    '''
    [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    [1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2]
    [0, 1, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7]
    '''


    for t in test_data:
        print( Solution().shortestToChar( S = t.string, C = t.character) )

    return



if __name__ == '__main__':

    test_bench()