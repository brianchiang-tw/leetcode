'''

Description:

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1



Example 2:

Input: "(())"
Output: 2



Example 3:

Input: "()()"
Output: 2



Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50

'''



class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        
        score_stack = []
        
        # record previous character
        prev = ''
        
        for ch in S:
            
            
            if ch == '(':
                # push 0 as occurrence of '('
                score_stack.append( 0 )
                
            else:
                
                if prev == ')':
                    # contiguous of ')', double the score
                    
                    summation = 0
                    while score_stack[-1] != 0:
                        summation += score_stack.pop()
                    
                    # pop latest 0 also known as lastest left brace (
                    score_stack.pop()
                    score_stack.append( 2*summation )
                        
                    
                else:
                    # single pair of (), add score by 1
                    
                    # pop latest 0 also known as lastest left brace (
                    score_stack.pop()
                    score_stack.append(1)
            
            # update previous character
            prev = ch
            
       
        # summation of all the scores in stack
        return sum(score_stack)



# n : the length of input string, S.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on ch, which is of O( n ),



## Space Complexity: O( n )
#
# The overhead in space is the storage for score_stack, which is of O( n ).



def test_bench():

    test_data = [
                    '()',
                    '(())',
                    '()()',
                    '(()(()))'
                ]

    # expected output:
    '''
    1
    2
    2
    6    
    '''

    for test_case in test_data:

        print( Solution().scoreOfParentheses(test_case) )
    
    return 



if __name__ == '__main__':

    test_bench()