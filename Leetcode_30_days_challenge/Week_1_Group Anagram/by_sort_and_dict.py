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


from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_dict = defaultdict( list )
        
        for s in strs:
            
            anagrams_dict[ ''.join( sorted(s) ) ].append( s )
            
        return [ anagrams_dict[key] for key in anagrams_dict ]



# n : the length of input list, strs.
# k : the average character length of word

## Time Complexity: O( n k log k )
#
# The overhead in time is the cost of is the loop of O ( n ), and the cost of sorting of O( k log k )
# It takes O( n k log k ) in total.

## Space Complexity: O( n * k)
#
# The overhead in space is the storage for dictionary, which is of O( n * k )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'list_of_string')
def test_bench():

    test_data = [
                    TestEntry( list_of_string = ["eat", "tea", "tan", "ate", "nat", "bat"] ),
                ]

    for t in test_data:

        print( Solution().groupAnagrams( t.list_of_string) )
    
    return



if __name__ == '__main__':

    test_bench()    


