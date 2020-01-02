'''

Description:

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 

If there are less than k characters left, reverse all of them. 

If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]

'''



class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        tokens = []
        
        while len(s) >= 2*k:
            
            tokens.append( s[ :2*k] )
            
            s = s[ 2*k: ]
            
        tail = s[::]
        
        tokens = [ ( t[:k][::-1] + t[k:] ) for t in tokens ]
        
        if len(tail) < k:
            tail = tail[::-1]
            
        else:
            tail = tail[:k][::-1] + tail[k:]
            
        
        concate_tokens = ''.join(tokens)
        
        return ( concate_tokens + tail )



# n : the length of input string

## Time Complixity:
# 
# The overhead in time is the while loop iteration, which is of O( n / k ) = O( n ) where k is constant.

## Space Complexity:
#
# The overhead in space is the storage for output sting, which is of the same length as input.
# Thus, it takes O( n ).



def test_bench():

    test_data = [
                    ( "abcde", 2 ),
                    ( "abcdef", 2 ),
                    ( "abcdefg", 2 ),
                    ( "abcdefgh", 2 ),
                ]

    # expected output:
    '''
    bacde
    bacdfe
    bacdfeg
    bacdfegh
    '''

    for test_pair in test_data:

        print( Solution().reverseStr( *test_pair ) )

    return 



if __name__ == '__main__':

    test_bench()