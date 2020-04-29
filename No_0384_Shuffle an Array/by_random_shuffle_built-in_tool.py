'''

Description:

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

'''


from typing import List
from random import shuffle

class Solution:

    def __init__(self, nums: List[int]):
        
        # copy to class member: self.array
        self.array = [ *nums ]
        
        # backup original sequence given by constructor
        self.origin = nums
        
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = [ *(self.origin) ]
        return self.array
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle( self.array )
        return self.array



# n : the length of input array

## Time Complexity: O( n )
#
# The overhead in time is the cost of shuffle and reset, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for class member, self.array, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    t = TestEntry( sequence = [1,2,3] )

    # reference output
    # this is a challenge about randomness, so any valid permutation of shuffling result is accpeted.

    '''
    [1, 3, 2]
    [1, 2, 3]
    [3, 2, 1]
    '''

    obj = Solution( t.sequence )
    print( obj.shuffle() )
    print( obj.reset() )
    print( obj.shuffle() )



if __name__ == '__main__':

    test_bench()