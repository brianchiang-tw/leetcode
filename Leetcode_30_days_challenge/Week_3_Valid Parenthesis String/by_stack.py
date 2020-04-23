'''

Description:

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.



Example 1:
Input: "()"
Output: True



Example 2:
Input: "(*)"
Output: True



Example 3:
Input: "(*))"
Output: True



Note:
The string size will be in the range [1, 100].

'''



class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # record the index of left brace
        stk = []
        
        # record the index of star symbol
        star = []
        
        for idx, char in enumerate(s):
            
            if char == '(':
                
                # left brace
                
                stk.append( idx )
                
            elif char == ')':
                
                # right brace
                
                if stk:
                    stk.pop()
                    
                elif star:
                    star.pop()
                    
                else:
                    return False
            else:
                
                # * star symbol
                
                star.append( idx )

        # pair left brace and star symbol                
        while stk and star:
            
            # Reject if left brace is on the right hand side of star symbol
            if stk[-1] > star[-1]:
                return False
            
            stk.pop()
            star.pop()

        # Accept if stack is empty.
        # Reject, otherwise.            
        return len(stk) == 0
                





# n : the chrarcter length of input string

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space os the storage for stacks, which is of O( n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')
def test_bench():

    test_data = [
                    TestEntry( string = "()" ),
                    TestEntry( string = "(*)" ),
                    TestEntry( string = "(*))" ),
                    TestEntry( string = "*)" ),
                    TestEntry( string = "(*" ),
                    TestEntry( string = "*(" ),
                    TestEntry( string = "*" ),
                ]


    # expected output:
    '''
    True
    True
    True
    True
    True
    False
    True
    '''

    for t in test_data:

        print( Solution().checkValidString( s = t.string) )
    
    return



if __name__ == '__main__':

    test_bench()                