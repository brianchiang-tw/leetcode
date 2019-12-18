'''

Description:

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string

'''



class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        # for pairing of '(' and ')'
        symbol_stack = []
        
        # storage for inner parentheses pairs
        inner_pair = []
        
        # sotrage for current pair group
        current_scan = ""
        
        for i, ch in enumerate(S):
        
            current_scan += ch
        
            if ch == '(':
                
                symbol_stack.append(ch)
                
            elif ch == ')':
            
                symbol_stack.pop()
                
                if len(symbol_stack) == 0:
                    # current pair group is completed
                    inner_pair. append( current_scan[1:-1] )
                    current_scan = ""
        
        
        # generate output string
        output_str = ''.join( inner_pair )
        
        return output_str



# N : the length of input string

## Time Complexity: O( N )
#
# The overhead in time is the for loop to scan each character on O( N )

## Space Complexity: O( N )
#
# The overhead in space is to maintain a stack for parenthesis pairing on O( N )


def test_bench():

    test_data = [ "(()())(())", "(()())(())(()(()))", "()()" ]

    # expected output:
    # the last one is empty string ""
    '''
    ()()()
    ()()()()(())

    '''

    for test_str in test_data :

        print( Solution().removeOuterParentheses(test_str) )

    return



if __name__ == '__main__':

    test_bench()