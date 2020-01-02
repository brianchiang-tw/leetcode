'''

Description:

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

'''

class Solution:
    def isMatch( self, s:str, p:str)->bool:

        size_of_s = len(s)
        size_of_p = len(p)

        # matching flag is a 2D array of ( size_of_s + 1 ) * ( size_of_p + 1 )
        matching_flag = [ [ False for j in range (size_of_p+1) ] for i in range(size_of_s+1) ]

        # Base case:
        # When both s and p are empty string, it is a match
        matching_flag[ 0 ][ 0 ] = True


        for j in range(1, size_of_p+1 ):

            # when p[j-1] is *, and s = empty string is match with p[0:j-1]
            if '*' == p[j-1] and matching_flag[0][j-1] is True:
                matching_flag[0][j] = True

        for i in range(1, size_of_s+1 ):
            for j in range(1, size_of_p+1 ):

                # if current character of p is '?', then the state is equal to the result of isMatch( s[:i-1], p[:j-1] )
                # if current character of p and last character of s is matched, then the state is eqaul to the result of isMatch( s[:i-1], p[:j-1] )
                if '?' == p[ j-1 ] or p[ j-1 ] == s[ i-1 ]:
                    matching_flag[ i][ j ] = matching_flag[ i-1 ][ j-1 ]

                # if current character of p is '*', then the state is equal to the result of isMatch( s[:i-1], p[:j] ) or isMatch( s[:i], p[:j] )
                if '*' == p[j-1]:
                    matching_flag[ i][ j ] = matching_flag[ i-1 ][ j ] or matching_flag[ i ][ j-1 ]

        # the match compare result of s and p
        return matching_flag[size_of_s][size_of_p]



# M : the size of input s
# N : the size of input p

## Time Complexity : O ( M*N )
#
# The major overhead is the double nested loop for i, j, which takes O( M ) and O( N ) respectively.

## Space Complexity: O( M*N )
#
# The major overhead is the space for record the solution state, which takes O( M*N ), with dynamic programming.



def test_bench():

    test_data = [ 
                    ("aa","a"),
                    ("aa","*"),
                    ("cb","?a"),
                    ("adceb","*a*b"),
                    ("acdcb","a*c?b")
                ]   

    # expected output:
    '''
    False
    True
    False
    True
    False
    '''



    for test in test_data:

        flag_of_match = Solution().isMatch( s = test[0], p = test[1] )

        print( flag_of_match )


    return



if __name__ == '__main__':

    test_bench()