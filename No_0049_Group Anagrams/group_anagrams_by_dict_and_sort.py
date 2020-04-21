'''

Description:

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''



from collections import Counter
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = defaultdict( list )
        
        
        for s in strs:
            
            # use sorted string with acsii order as key of dictionary
            ordered_s = ''.join(sorted(s))
            
            anagram_dict[ordered_s].append( s )
                
        return anagram_dict.values()


# n : the number of strings in input strs.
# k : the average character length of strings

## Time Complexity: O( n k log k)
#
# The overhead in time is the for loop, iterating on strs, which is of O( n ),
# and the cost of sorted(s), which is of O( k log k ).
# It takes O( n k log k ) in total.

## Space Complexity: O( n * k)
#
# The overhead in space is the storage for dictionary, which is of O( n * k )
                

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'input_string')
def test_bench():

    test_data = [
                    TestEntry( input_string = ["eat", "tea", "tan", "ate", "nat", "bat"] )
                ]

    # expected output:
    '''
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    '''

    for t in test_data:

        print( Solution().groupAnagrams( t.input_string) )

    return



if __name__ == '__main__':

    test_bench()