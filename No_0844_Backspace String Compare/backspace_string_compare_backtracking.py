'''

Description:

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

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
    
    def backspaceCompare(self, S, T):
        
        i, j = len(S) - 1, len(T) - 1
        backward_S, backward_T = 0, 0
        
        while True:
            while i >= 0 and (backward_S or S[i] == '#'):
                
                if S[i] == '#':    
                    backward_S += 1
                
                else:
                    backward_S -= 1
                
                i -= 1
                
            while j >= 0 and (backward_T or T[j] == '#'):
                
                if T[j] == '#':
                    backward_T += 1
                    
                else:
                    backward_T -= 1
                
                j -= 1
                
            if not (i >= 0 and j >= 0 and S[i] == T[j] ):
                
                return i == -1 and j == -1
            
            i, j = i - 1, j - 1



# N : the max length of input (s, t)

## Time Compleixty: O( N )
#
# The overhead in time is the inner while loops to iterate string S and T of oerder O( N )

## Space Complexity: O( 1 )
#
# The overhead in space is to maintain loop variable i, j and backtracking variable backward_S, backward_T.
# All of them are fixed size with O( 1 )



def test_bench():

    test_data = [
                    ("ab#c", "ad#c"),
                    ("ab##", "c#d#"),
                    ("a##c", "#a#c"),
                    ("a#c", "b"),
                ]

    # expected output:
    '''
    True
    True
    True
    False
    '''


    for str_pair in test_data:

        print( Solution().backspaceCompare(*str_pair) )

    return



if __name__ == '__main__':

    test_bench()