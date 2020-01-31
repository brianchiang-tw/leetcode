class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = [ False for i in range(1000001) ]

        
    def add(self, key: int) -> None:
        
        if not self.hash_set[key]:
            self.hash_set[key] = True

            
    def remove(self, key: int) -> None:
        
        if self.hash_set[key]:
            self.hash_set[key] = False

            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
        if self.hash_set[key]:
            return True
        else:
            return False
        class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = [ False for i in range(1000001) ]

        
    def add(self, key: int) -> None:
        
        if not self.hash_set[key]:
            self.hash_set[key] = True

            
    def remove(self, key: int) -> None:
        
        if self.hash_set[key]:
            self.hash_set[key] = False

            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
        if self.hash_set[key]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)