'''

Description:

ou are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

 

Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"



Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
 

Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100


Hint 1:

Intuitively performing all shift operations is acceptable due to the constraints.



Hint 2:

You may notice that left shift cancels the right shift, so count the total left shift times (may be negative if the final result is right shift), and perform it once.

'''



from typing import List
from collections import deque

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        right_shift = 0
        left, right, size = 0, 1, len(s)
        
        if size == 1:
            # Quick response for simple case
            return s
        
        # compute final shift offset
        
        # positve value means right shift
        # negative value means left shift
        
        for dir, offset in shift:
            
            if dir == left:
                right_shift -= offset
            else:
                right_shift += offset
                
        # eliminate redundant over-size shift                
        right_shift = right_shift % size
        

        # convert immutable string to mutable double ended queue
        res = deque( [*s] )
        
        # perforam shifting       
        res.rotate( right_shift )
        
        # convert back to string type and output
        return ''.join( res )
    



# m : the character length of string
# n : the length of shift requests

## Time Complexity: O( m * n )
#
# The overhead in time is the cost of shifting, which is of O( m ), and the cost of shift vector compuation, which is of O( n ).
#
# It takes O( m * n ) in total.

## Space Complexity: O( m )
#
# The overhead in space is the storage for deque and output string, which are of O( m )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string shift')

def test_bench():

    test_data = [
                    TestEntry( string = "abc", shift = [[0,1],[1,2]] ),
                    TestEntry( string = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]] ),
                    TestEntry( string = "a", shift = [[1,1],[1,1],[0,2],[1,3]]  ),
                ]


    # expected output:
    '''
    cab
    efgabcd
    a
    '''

    for t in test_data:

        print( Solution().stringShift( s = t.string, shift = t.shift ) )

    return



if __name__ == '__main__':

    test_bench()    