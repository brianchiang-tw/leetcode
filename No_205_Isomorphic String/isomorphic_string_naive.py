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
        
        if s == "" and t == "":
            # corner case:
            # both s and t are empty strings
            return True
        
        
        dict_s_t = dict()

        # linear scan each character and check mapping relation
        for i in range( len(s ) ):
            
            look_up = dict_s_t.get( s[i], None) 
            if look_up is None:
                # first time
                
                if t[i] not in dict_s_t.values():
                    # if mapping is no collided
                    dict_s_t[ s[i] ] = t[i]
                else:
                    # if mapping is collided with an existing one mapping relation
                    return False
                
            else:
                # already has mapping
                if dict_s_t[ s[i] ] != t[i]:
                    return False
                
        else:
            return True

# N : the length of string s or t

## Time Complexity : O( N )
#
# The overhead is the for loop over strings of O( N )
# The lookup and creation of dictionry entry is O( 1 )

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