'''

Description:

Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.

'''



from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.comb = [ *combinations(characters, combinationLength)]
        self.idx = 0
        
    def next(self) -> str:
        
        answer = ''.join( self.comb[self.idx] )
        self.idx += 1
        return answer
        

    def hasNext(self) -> bool:
        
        if self.idx != len(self.comb):
            return True
        
        else:
            return False



# n : the length of input, characters

## Time Complexity: O( n^n )
#
# The overhead in time is the cost of combination, which is of O( n^n ).

## Space Complexity: O( C(n, k) )
#
# The overhead in space is the storage for all possible combinations, which is of O( n ).

import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        iterator = CombinationIterator("abc", 2) # creates the iterator.
        
        result = iterator.next()         # returns "ab"
        self.assertEqual(result, 'ab')

        result = iterator.hasNext()      # returns true
        self.assertEqual(result, True)

        result = iterator.next()         # returns "ac"
        self.assertEqual(result, 'ac')

        result = iterator.hasNext()      # returns true
        self.assertEqual(result, True)
        
        result = iterator.next()         # returns "bc"
        self.assertEqual(result, 'bc')

        result = iterator.hasNext()      # returns false
        self.assertEqual(result, False)


if __name__ == '__main__':

    unittest.main()