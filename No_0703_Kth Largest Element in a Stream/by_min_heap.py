'''

Description:

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.

'''



from typing import List
from heapq import heapify, heappop, heappush, heappushpop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.arr = nums
        
        heapify( self.arr) 
        
        # Keep popping smaller elemnts till size = k
        while len( self.arr ) > self.k:
            heappop( self.arr )

    def add(self, val: int) -> int:
        
        heap_top = 0
        
        # Always keep heap size = k
        # Top element = kth largest element
        if len( self.arr ) < self.k:
            heappush( self.arr, val)
        else:
            heappushpop( self.arr, val)
        
        return self.arr[heap_top]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



# n : the length of input nums
# k : the value of specified order

## Time Complexity:
#
# O( n log n ) for __init()__
# O( log k ) for add

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array k add_sequence')
def test_bench():

    
    t = TestEntry( array = [4,5,8,2], k = 3, add_sequence = [3, 5, 10, 9, 4])
    
    obj = KthLargest( k = t.k, nums = t.array )

    # expected output:
    '''
    4
    5
    5
    8
    8
    '''

    for number in t.add_sequence:
        print( obj.add( number ) )

    return



if __name__ == '__main__':

    test_bench()