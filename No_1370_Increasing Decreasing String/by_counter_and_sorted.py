'''

Description:

Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

 

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
Example 3:

Input: s = "leetcode"
Output: "cdelotee"
Example 4:

Input: s = "ggggggg"
Output: "ggggggg"
Example 5:

Input: s = "spo"
Output: "ops"
 

Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.

'''





from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        
        size = len(s)
        
        if size == 1:
            
            # Quick response for single character input
            return s
        
        char_occ_dict = Counter(s)
        
        sorted_keys = sorted( char_occ_dict.keys() )
        
        result, counter = [ ], 0
        
        while counter != size:
            
            # Ascending phase
            for unique_char in sorted_keys:
                
                if char_occ_dict[unique_char] > 0:
                    result.append( unique_char )
                    char_occ_dict[unique_char] -= 1
                    counter += 1
            
            # Descending phase
            for unique_char in sorted_keys[::-1]:
                
                if char_occ_dict[unique_char] > 0:
                    result.append( unique_char )
                    char_occ_dict[unique_char] -= 1
                    counter += 1
                    
        return ''.join( result )



# n : the character length of input string, s
# k : the number of unique characters of input string, s

## Time Complexity: O( n + k log k )
#
# The overhead in time is the cost for dictionary building, of O( n ), and sorted, of O( k log k).
# It takes O( n + k log k ) in total.

## Spaec Complexity: O( n )
#
# The overhead in space is the storage for dictionary, char_occ_dict, and output list result, which are of O( n )


from collections import namedtuple
TestEntry = namedtuple('TestEntr', 'string')
def test_bench():

    test_data = [
                    TestEntry( string = "aaaabbbbcccc" ),
                    TestEntry( string = "rat" ),
                    TestEntry( string = "leetcode" ),
                    TestEntry( string = "ggggggg" ),
                    TestEntry( string = "spo" )
                ]


    # expected output:
    '''
    abccbaabccba
    art
    cdelotee
    ggggggg
    ops
    '''

    for t in test_data:

        print( Solution().sortString( t.string ) )

    return



if __name__ == '__main__':

    test_bench()

