'''

Description:

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:

Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]



Input: S = "3z4"
Output: ["3z4", "3Z4"]



Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

'''



from typing import List
from string import ascii_letters

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        def next_alphabet( s: str):
            # Generator to yield next index of alphabet, if not, raise StopIteration
        
            for idx, char in enumerate(s):
                if char in ascii_letters:
                    yield idx
        
        
        def permutation_factory( s:str ):
        
            try:
                # General case:
                # DFS with backtracking
                idx = next(next_alphabet(s))
                
                permu = permutation_factory( s[idx+1:])
                
                next_permu = []
                
                # Flip current alphabet and concatenate with perumutation
                for p in permu:
                    next_permu.append( s[:idx] + s[idx].lower() + p )
                    next_permu.append( s[:idx] + s[idx].upper() + p )
                    
                return next_permu
            
            except StopIteration:
                # Base case: 
                # No alphabet, direct return current string
                return [s]
         
        # ----------------------------
        return permutation_factory(S)



# n : the length of input string
# k : the number of alphabet characters in input string

## Time Complexity: O( n * 2^k )
#
# The overhead in time is the cost of permutation generation, which is of O( n * 2^k )

## Space Complexity: O( n * 2^k )
#
# The overhead in space is the storage for all permuation output, which is of O( n * 2^k )


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'string')

def test_bench():

    test_data = [
                    TestEntry( string = "a1b2"),
                    TestEntry( string = "3z4"),
                    TestEntry( string = "12345"),
                ]

    # expected output:
    '''
    ['a1b2', 'A1b2', 'a1B2', 'A1B2']
    ['3z4', '3Z4']
    ['12345']
    '''

    for t in test_data:
        print( Solution().letterCasePermutation( S = t.string) )


    return



if __name__ == '__main__':

    test_bench()