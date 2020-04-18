'''

Description:

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

'''



class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # store the indices of '('
        stk = []
        
        # store the indices of '*'
        star = []
        
        
        for idx, char in enumerate(s):
            
            if char == '(':
                stk.append( idx )
                
            elif char == ')':
                
                if stk:
                    stk.pop()
                elif star:
                    star.pop()
                else:
                    return False
            
            else:
                star.append( idx )
        
        
        # cancel ( and * with valid positions, i.e., '(' must be on the left hand side of '*'
        while stk and star:
            if stk[-1] > star[-1]:
                return False
        
            stk.pop()
            star.pop()
        
        
        # Accept when stack is empty, which means all braces are paired
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