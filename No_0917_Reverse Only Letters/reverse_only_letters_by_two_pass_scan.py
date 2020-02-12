'''

Description:

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"



Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"



Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "

'''



class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        
        char_string = ""
        
        # collect alphabet letters
        for ch in S:
            if ch.isalpha():
                char_string += ch
                
                
        # index points to last alphabet letter
        index = len(char_string)-1
        
        # output string with reverse alphabet letter only
        reverse_letter_only = ""
        
        # revese string on character base
        for ch in S:
            
            if ch.isalpha():
                # alphabet letter, reverse the order
                reverse_letter_only += char_string[index]
                index -= 1
                
            else:
                # non alphabet letter, keep the same
                reverse_letter_only += ch
                
        
        return reverse_letter_only



# n : the character length of input string, S.

## Time Complexity: O( n )
#
# The overhead in time is the for loops, iterating on ch, which are of O( n )


## Space Complexity: O( n )
#
# The overhead in space is the storage for strings, 
# char_string, as well as reverse_letter_only, which are of O( n ).



def test_bench():

    test_data = [
                    "ab-cd",
                    "a-bC-dEf-ghIj",
                    "Test1ng-Leet=code-Q!"
                ]

    # expected output:
    '''
    dc-ba
    j-Ih-gfE-dCba
    Qedo1ct-eeLg=ntse-T!
    '''

    for test_string in test_data:

        print( Solution().reverseOnlyLetters(test_string) )
    
    return 



if __name__ == '__main__':

    test_bench()