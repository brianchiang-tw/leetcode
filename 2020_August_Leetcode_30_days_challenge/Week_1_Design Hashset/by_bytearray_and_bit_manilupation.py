'''

Description:

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.

'''



class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = bytearray(125001)

        
    def add(self, key: int) -> None:
        
        quotient, remainder = divmod(key, 8)
		
        if not self.hash_set[quotient] & (1 << remainder):
			
			# set to True for existence of incoming element
            self.hash_set[quotient] |= (1 << remainder)

            
    def remove(self, key: int) -> None:
        
        quotient, remainder = divmod(key, 8)
		
        if self.hash_set[quotient] & (1 << remainder):
		
			# clear to False for removal
            self.hash_set[quotient] &= ~(1 << remainder)

            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
		
        quotient, remainder = divmod(key, 8)
		
		# check the flag for existence judgement
        if self.hash_set[quotient]& (1 << remainder):
            return True
			
        else:
            return False




import unittest

class Testing(unittest.TestCase):

    def test_case_1(self):

        hashSet = MyHashSet()
        hashSet.add(1)         
        hashSet.add(2)         

        result = hashSet.contains(1)     # returns true
        self.assertEqual(result, True)

        result = hashSet.contains(3)     # returns false (not found)
        self.assertEqual(result, False)

        hashSet.add(2)          
        
        result = hashSet.contains(2)     # returns true
        self.assertEqual(result, True)

        hashSet.remove(2)          

        result = hashSet.contains(2)     # returns false (already removed)
        self.assertEqual(result, False)



if __name__ == '__main__':

    unittest.main()