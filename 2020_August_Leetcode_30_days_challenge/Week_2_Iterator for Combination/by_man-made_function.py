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



class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        
        source = [*characters]

        # -----------------------------------
        def dfs(cur_comb, src, result):
            
            if len(cur_comb) == combinationLength:
                yield cur_comb
                return

                
            for idx, char in enumerate(src):
                src[0], src[idx] = src[idx], src[0]
                
                yield from dfs(cur_comb+src[0], src[idx+1:], result)
                
                src[0], src[idx] = src[idx], src[0]
            
            return

        # -----------------------------------

        self.length = combinationLength
        self.combination = iter(dfs(cur_comb='', src=source, result=[]))
        self.next_element = None
        
        

    def next(self) -> str:
        
        if self.next_element:
            result = self.next_element
            self.next_element = None
            return result
        
        else:
            return next(self.combination)
    
        

    def hasNext(self) -> bool:
        
        if self.next_element:
            return True
        
        try:
            self.next_element = next(self.combination)
            return True
            
        except StopIteration:
            return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()



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