'''

Description:

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.



Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.



Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true



Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
The characters of name and typed are lowercase letters.

'''



class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        idx_src= 0
        
        size_src, size_type = len(name), len(typed)
        
        for idx_type, char_type in enumerate(typed):
            
            if idx_src < size_src and name[idx_src] == char_type:
                # current type char is matched with friend's name char
                idx_src += 1 
                
            elif idx_type == 0 or typed[idx_type] != typed[idx_type-1]:
                # If first character mismatch, or it is not long-pressed repeated characters
                # Reject
                return False
        
        # Accept if all character is matched with friend name
        return idx_src == size_src
    


# t : the character lenth of input string, typed.

## Time Complexity: O( t )
#
# The overhead in time is the cost of linear scan on typed, which is of O( t ).

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for two-pointers, which is of O( 1 ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry','friend_name typed_name')

def test_bench():

    test_data = [
                    TestEntry( friend_name = "alex", typed_name = "aaleex" ),
                    TestEntry( friend_name = "saeed", typed_name = "ssaaedd" ),
                    TestEntry( friend_name = "leelee", typed_name = "lleeelee" ),
                    TestEntry( friend_name = "laiden", typed_name = "laiden" ),
                ]


    # expected output:
    '''
    True
    False
    True
    True
    '''

    for t in test_data:

        print( Solution().isLongPressedName( name = t.friend_name, typed = t.typed_name ) )

    return



if __name__ == '__main__':

    test_bench()    