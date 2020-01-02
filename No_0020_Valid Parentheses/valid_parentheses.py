class Solution:
    def isValid(self, s: str) -> bool:
        
        
        # corner case check
        if len(s) == 0:
            return True
        
        
        left_braces     = [ '(', '[', '{']
        right_braces    = [ ')', ']', '}']
        
        pair_checking_stack = []
        
        for char in s:
            
            if char in left_braces:
                # left braces
                pair_checking_stack.append( char )
                
            elif char in right_braces:
                # right braces
                
                if len(pair_checking_stack) == 0:
                    # stack is empty, no chance to match
                    return False
                
                else:
                    # try to get the top element of stack
                    top_of_stack = pair_checking_stack[-1]
                
                
                # get the index of left brace from ( [ { 
                pair_of_left = left_braces.index( top_of_stack )
                
                # get the index of right brace from ) ] }
                pair_of_right = right_braces.index( char )
                
                if pair_of_left != pair_of_right:
                    # mis-match with left braces on the top of stack
                    
                    return False
                
                else:
                    # match with left braces on the top of stack
                    # pop the top of stack
                    
                    pair_checking_stack.pop()
                    
            else:
                # skip other characters except for () [] {}
                continue
        
        
        
        if len(pair_checking_stack) == 0:
            return True
        
        else:
            return False


# N : the length of input string s

## Time Complexity: O( N )
#
# The overhead is the for loop to linear scan each character in s


## Space Complexity: O( N )
#
# The overhead is the variable to keep a stack to record the left braces including '(', '[' and '{'
# The size of stack is at most O( N )


def test_bench():

    test_data = [
                    "()",
                    "()[]{}",
                    "(]",
                    "([)]",
                    "{[]}"
                ]

    # expected output:
    # Y
    # Y
    # N
    # N
    # Y


    for test_string in test_data:

        result = Solution().isValid( test_string )

        if result :
            print("Y")
        else:
            print("N")

    return



# entry point of main
if __name__ == '__main__':

    test_bench()