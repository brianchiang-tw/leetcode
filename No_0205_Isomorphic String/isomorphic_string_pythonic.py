'''

Description:

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_relation = dict( zip(s, t) )
        
        # check for overladpped mapping
        map_range = map_relation.values()
        
        if len( map_range) != len( set(map_range) ):
            return False
        
        # check mapping from s to t is coherent 
        return ''.join( [ map_relation[ s[i] ] for i in range( len(s) ) ] ) == t

# N : the length of string s or t

## Time Complexity : O( N )
#
# The overhead is the for dictionary creation and join of list comprehension of O( N )
# The lookup of dictionry entry is O( 1 )

## Space Complexity : O( N )
#
# The overhead is the space for looping variable of O(1) and dictionary with size at most O( N )


def test_bench():

    test_data = [
                    ( "add", "egg"),
                    ( "add", "top"),
                    ( "add", "moo")
                ]

    # expected output:
    '''
    True
    False
    True
    '''


    for test in test_data:

        is_isomorphic = Solution().isIsomorphic( *test )

        print( is_isomorphic)

    return



if __name__ == '__main__':

    test_bench()