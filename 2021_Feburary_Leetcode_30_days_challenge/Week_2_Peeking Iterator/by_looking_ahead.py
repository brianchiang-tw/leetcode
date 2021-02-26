'''

Description:

Design an iterator that supports the peek operation on a list in addition to the hasNext and the next operations.

Implement the PeekingIterator class:

PeekingIterator(int[] nums) Initializes the object with the given integer array nums.
int next() Returns the next element in the array and moves the pointer to the next element.
bool hasNext() Returns true if there are still elements in the array.
int peek() Returns the next element in the array without moving the pointer.
 

Example 1:

Input
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 2, 2, 3, false]

Explanation
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
peekingIterator.hasNext(); // return False
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
All the calls to next and peek are valid.
At most 1000 calls will be made to next, hasNext, and peek.
 

Follow up: How would you extend your design to be generic and work with all types, not just integer?

'''


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int



class PeekingIterator:

    def __init__(self, iterator):

        self.iterator = iterator

        # pre-store next one element by looking ahead
        if self.iterator.hasNext():

            # still have next element
            self.next_one = self.iterator.next()

        else:

            # meet the end
            self.next_one = None
    

    def peek( self ):

        # return the pre-stored element
        return self.next_one

    
    def next( self ):

        # backup original pre-stored element
        target = self.next_one

        # keep getting next one element
        if self.iterator.hasNext():
            self.next_one = self.iterator.next()

        else:
            self.next_one = None
        
        return target

    
    def hasNext(self):

        # judge by the existence of pre-stored element

        if self.next_one:
            return True
        
        else:
            return False


## Time Complexity: O( 1 )
#
# The overhead in time is the cost of pre-store of next element, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for pre-store of next element, which is of O( 1 )