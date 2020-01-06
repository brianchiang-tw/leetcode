'''

Description:

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]
 

Note:

1 <= S.length <= 10000
S only contains characters "I" or "D".

'''



from collections import deque
from typing import List
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        numbers = deque( list( range( len(S)+1 ) ) )
        
        output = []
        
        for ch in S:
            
            if ch == 'I':
                # Increaing, select min, and push it into output
                output.append( numbers.popleft() )
                
            else:
                # Decreasing, select Max, and push it into output
                output.append( numbers.pop() )
                
    
        # last element
        output.append( numbers.pop() )
        
        return output



# n : the length of input s 

## Time Compleity: O( n )
#
# The overhead in time is the for loop iterating on ch, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for list, output, which is of O( n ).



def test_bench():

    test_data = [
                    "IDID",
                    "III",
                    "DDI"
                    "DIDIDIDI"
                ]


    # expected output:
    '''
    [0, 4, 1, 3, 2]
    [0, 1, 2, 3]
    [11, 10, 0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
    '''

    for test_sequence in test_data:

        print( Solution().diStringMatch(test_sequence) )

    return 



if __name__ == '__main__':

    test_bench()