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
        
        # start from index 0
        index_of_s = 0
        # start from index 0
        index_of_p = 0

        # the first index of s when seeing a '*' in p
        s_star_match_index = 0

        # the latest index of '*' in p
        p_last_star_index = None

        size_of_s = len(s)
        size_of_p = len(p)

        # saan each character of s
        while index_of_s < size_of_s:

            
            if index_of_p < size_of_p and p[ index_of_p ] in (s[index_of_s], '?'):
                # if p[ index_of_p ] == s[ index_of_s ] or p[ index_of_p ] == '?'


                index_of_s += 1
                index_of_p += 1
            
            
            elif index_of_p < size_of_p and p[ index_of_p ] == '*':
                # p[ index_of p ] doesn't match (s[ index_of_s ] or '?')
                # if p[ index_of p ] is '*'
                
                # record current index of s and p
                s_star_match_index = index_of_s
                p_last_star_index = index_of_p

                # p moves forward
                index_of_p += 1

            elif  p_last_star_index != None:
                # use the latest '*' = p[p_last_star_index] to match s[s_star_match_index]

                # s moves forward
                index_of_s = s_star_match_index + 1

                # update star match index of s
                s_star_match_index += 1

                # update index of p
                index_of_p = p_last_star_index  + 1

            else:
                return False

        
        while index_of_p < size_of_p and '*' == p[index_of_p]:
            # keep moving forward if there are redundant * in p
            index_of_p += 1

        if index_of_p == size_of_p:
            return True

        else:
            return False




# M : the size of input s
# N : the size of input p

## Time Complexity : O ( M + N )
#
# The major overhead are those two loops.
# First one is while loop for s with O( M ), the other is while loop for p with O( N )
# In summary, total time complexity is O( M + N )

## Space Complexity: O( 1 )
#
# The major overhead is the space for string operation index with O(1), 
# such as index_of_s, index_of_p, s_star_match_index as well as p_last_star_index.




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