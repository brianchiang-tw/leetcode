class Solution:
    

    
    def removeDuplicates(self, s: str, k: int) -> str:
        
        char_stack = [ ['bottom', 0] ]
        
        for char in s:
            
            if char == char_stack[-1][0]:
                # update last character's length of adjancy
                #last_char, last_adj_len = char_stack.pop()
                #char_stack.append( (last_char, last_adj_len+1) )
                char_stack[-1][1] += 1
            
            else:
                # push character with length of adjancy = 1
                char_stack.append( [ char, 1] )
                
            
            if char_stack[-1][1] == k:
                # pop last character if it has repeated k times
                
                char_stack.pop()
        
        
        
        output_str = ""
        for i in range( len(char_stack) ):
            output_str += char_stack[i][0] * char_stack[i][1]
            
        
        return output_str



# n : the length of input s

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on char, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for the char_stack, which if of O( n )



def test_bench():

    test_data = [
                    ("abcd", 2),
                    ("deeedbbcccbdaa",3),
                    ("pbbcggttciiippooaais", 2)
                ]

    # expected output:
    '''
    abcd
    aa
    ps
    '''


    for test_str, k in test_data :

        print( Solution().removeDuplicates(test_str, k) )

    return 



if __name__ == '__main__':

    test_bench()