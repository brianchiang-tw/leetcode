'''

Description:


Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

'''



class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        tokens = list( str.split() )
        
        if len(pattern) != len(tokens):
            # length of pattern and str are mis-matched.
            return False
        
        p_s_pair = list( zip( pattern, tokens) )
        
        mapping_dict = dict()
        range_set = set()
        
        for patrn, token in p_s_pair:
            
            result = mapping_dict.get( patrn, None)
            
            if result:
                if result != token:
                    # reject one-to-N mapping
                    return False
                
            else:
                if token in range_set:
                    # reject N-to-one mapping
                    return False
                
                mapping_dict[patrn] = token
                range_set.add( token )
                
        return True



# n : the length of input pattern

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on (patrn, token), which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, mapping_dict, which is of O( n )


def test_bench():

    test_data = [
                    ( "abba", "dog cat cat dog" ),
                    ( "abba", "dog cat cat fish" ),
                    ( "abba", "dog dog dog dog" ),
                    ( "aaa", "aa aa aa aa" )
                ]

    # expected output:
    '''
    True
    False
    False
    False
    '''

    for test_pair in test_data:

        print( Solution().wordPattern(*test_pair) )

    return 



if __name__ == '__main__':

    test_bench()

        
        