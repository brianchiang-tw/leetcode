'''

Description:

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

'''



class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # list to save numbers
        self.number_list = []
        
        # dictionary
        # key: number
        # value: index of number in self.number_list
        self.number_dict = dict()
        
        # size of data structure
        self.size = 0
        
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        
        if val in self.number_dict:
            return False
        
        else:            
            
            # record new element index in dictionary
            self.number_dict[ val ] = self.size
            
            # append new element into list
            self.number_list.append( val )
            
            # update size of collection
            self.size += 1
            
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if val not in self.number_dict:
            return False
        
        else:

            # To reach O(1) performance, use technique of element swap, and pop on tail
            
            # get the index of element with value
            index_of_val = self.number_dict[val]
            
            
            # update index of last_element
            self.number_dict[ self.number_list[-1] ] = index_of_val
            
            
            # swap val with last element of number_list
            self.number_list[-1], self.number_list[index_of_val] = self.number_list[index_of_val], self.number_list[-1]
            
            
            # remove val from list by popping last
            self.number_list.pop()
            
            # remove val from dictionary by deleting key
            del self.number_dict[val]
        
            # update size of collection
            self.size -= 1
        
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return random.choice( self.number_list )



# Time Complexity: O( 1 )
#
# The insert, remove, getRandom is of O(1) with natual property of list and dictionary

## Space Complexity: O( 1 ) amortized
#
# The overhead in space is O( 1 ) amortized for each insert, remove and getRandom.


# The output is not deterministic, therefore local test bench is not provided.