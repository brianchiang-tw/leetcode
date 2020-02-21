
from functools import reduce
from operator import add
from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        unique_chars = set(A[0])

        common_char_occ = [ [char] * min([string.count(char) for string in A]) for char in unique_chars]

        result = reduce( add, common_char_occ)
        
        return result



# n : the length of input list, A
# k : the average length of words in A

## Time Complexity: O( n * k^2 )
#
# The overhead in time is the cost of list comprehension iteration, which is of ( n * k),
# and the cost of string.count( char ), which is of O( k ).
#
# It takes O( n * k^2 ) in total


## Space Complexity: O( k )
#
# The overhead in space is the storage for set, unique_chars, and
# result list, which are of O( k ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence_of_string')
def test_bench():

    test_data = [
                    TestEntry( ["bella","label","roller"] ),
                    TestEntry( ["cool","lock","cook"] ),
                    TestEntry( ["leet", "code", "leetcode"] )
                ]

    for t in test_data:

        print( Solution().commonChars(t.sequence_of_string) )

    return



if __name__ == '__main__':

    test_bench()