'''

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]



Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter

'''



from collections import Counter
from functools import reduce
from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        # Base case:
        A[0] = Counter(A[0])
        
        # functor to express intersection of Counter
        func = lambda x, y: x &Counter(y)
        
        # update dictionary for common characters by itersection of Counter
        str_occ_dict = reduce( func, A)
        
        return list( char for char in str_occ_dict for _ in range(str_occ_dict[char]) )



# n : the length of input list, A
# k : the average length of words in A

## Time Complexity: O( n * k^2 )
#
# The overhead in time is the cost of reduce, which is of ( n ),
# and the cost of func execution, which is of O( k^2 ) for dictionary building and intersection.


## Space Complexity: O( k )
#
# The overhead in space is the storage for dictionary, which is of O( k ).


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