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
    
    def final_str(self, s:str)->str:
        
        stk = []
        
        for ch in s:
            
            if ch != '#':
                stk.append( ch )
            else:
                if len( stk ) != 0:
                    stk.pop()
                
        #print("stk", stk)
        
        return "".join(stk)
    
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        final_s = self.final_str(S)
        final_t = self.final_str(T)
        
        return ( final_s == final_t )



# N : the max length of input (s, t)

## Time Compleixty: O( N )
#
# The overhead in time is the for loop in function final_str() of oerder O( N )

## Space Complexity: O( N )
#
# The overhead in space is to maintain a stack for backsapce,
# while the size of stack growth in order of O( N )



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