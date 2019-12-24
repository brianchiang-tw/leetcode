'''

Description:

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

'''



class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        char_stack = []
        
        for char  in S:
            
            if char_stack and char_stack[-1] == char:
                # top of stack is the same as next character
                # eliminate duplicates 
                char_stack.pop()  
                
            else:
                # no adjacent repetition characters
                # push next character into stack
                char_stack.append( char )
            
            
        return ''.join(char_stack)


# n : the length of input string

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on S, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the stack to store characters, which is up to O( n )


def test_bench():

    test_data = [ "abbaca", "abbccddeeef", "aabcdef" ]

    # expected output:
    '''
    ca
    aef
    bcdef
    '''

    for test_s in test_data:

        print( Solution().removeDuplicates(test_s) )

    return



if __name__ == '__main__':

    test_bench()
