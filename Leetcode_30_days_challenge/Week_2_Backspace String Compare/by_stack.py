'''

Description:

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".



Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".



Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".



Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".



Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?


'''




class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def final_string( s: str) -> str:

            stk = []

            for char in s:

                if char != '#':
                    
                    # append character into stack
                    stk.append( char )
                
                elif stk:
                    # backspace when we meet '#'
                    stk.pop()

            return ''.join( stk )

        # -----------------------------------------------

        return final_string( S ) == final_string( T )



# n : the character length of S + T 

## Time complexity: O( n )
#
# The overhead in time is the cost of stack operation, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for stack, which is of O( n )



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'S T')

def test_bench():



    test_data = [
                    TestEntry( S = "ab#c", T = "ad#c" ),
                    TestEntry( S = "ab##", T = "c#d#" ),
                    TestEntry( S = "a##c", T = "#a#c" ),
                    TestEntry( S = "a#c", T = "b" ),
                ]        

    # expected output:
    '''
    True
    True
    True
    False
    '''

    for t in test_data:

        print( Solution().backspaceCompare( S = t.S, T = t.T ) )
    
    return



if __name__ == '__main__':

    test_bench()    