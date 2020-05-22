'''

Description:

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.



Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.



Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''



from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        ## dictionary:
        # key: character
        # value: occurrence of character

        char_occ_dict = Counter( s )
        size = len(char_occ_dict)

        
        output_list = []
        char_occ_pair =  char_occ_dict.most_common(size)
        
        # output character with occurrence, from high frequency to low frequency
        for char, occ in char_occ_pair:
            output_list += [ char ]*occ
        
        
        return ''.join( output_list )



# n : the length of input string

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of occurrence sorting, which is of O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary and char_occ_pair, which are of O( n )

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')

def test_bench():

    test_data = [
                    TestEntry( string = "tree" ),           
                    TestEntry( string = "cccaaa" ),
                    TestEntry( string = "Aabb"),
                ]

    # expected output:
    '''
    eetr
    cccaaa
    bbAa
    '''

    for t in test_data:

        print( Solution().frequencySort( s = t.string ) )
    
    return



if __name__ == '__main__':

    test_bench()
