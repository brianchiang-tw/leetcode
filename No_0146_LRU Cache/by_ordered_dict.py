'''

Description:

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''




from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        
        self.size = capacity
        
        self.lru_cache = OrderedDict()
        

    def get(self, key: int) -> int:
        
        if key not in self.lru_cache:
            return -1
        
        else:
            # refresh the entry with given key
            self.lru_cache.move_to_end( key )
            
            return self.lru_cache[ key ]
        

    def put(self, key: int, value: int) -> None:
        
        if key not in self.lru_cache:
            
            if len( self.lru_cache ) >= self.size :
                # pop the least used entry
                self.lru_cache.popitem( last = False )

        else:
            self.lru_cache.move_to_end( key )
        
        self.lru_cache[ key ] = value



# k : the size of LRU Cache

## Time Complexity:
# O(1) for get() due to dictionary data strucutre
# O(1) for put() due to dictionary data strucutre


## Space Complexity:
#
# O( k ) for the storage of ordered dictionary



def test_bench():

    # create a LRU Cache with size = 2
    cache = LRUCache( 2 )

    # expected output
    '''
    1
    -1
    -1
    3
    4
    '''


    cache.put(1, 1)
    cache.put(2, 2)
    print( cache.get(1) )   # returns 1
    cache.put(3, 3)         # evicts key 2
    print( cache.get(2) )   # returns -1 (not found)
    cache.put(4, 4)         # evicts key 1
    print( cache.get(1) )   # returns -1 (not found)
    print( cache.get(3) )   # returns 3
    print( cache.get(4) )   # returns 4



if __name__ == '__main__':

    test_bench()    