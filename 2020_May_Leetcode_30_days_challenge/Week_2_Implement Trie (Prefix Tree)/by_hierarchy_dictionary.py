'''

Description:

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

'''



class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        def helper( char, table ):
            
            if char not in table:
                table[char] = {}
            

            return table[char]
        
        # -----------------------
        
        # update new word into trie
        table = self.trie
        for char in word:
            table = helper( char, table)
        
        # use '@' as ending symbol
        table['@'] = {}
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        def helper( char, table):
            
            if char in table:
                return table[char]
            else:
                return None
            
        # -----------------------
        
        # search word in trie
        table = self.trie
        
        for char in word:
            table = helper( char, table)
            
            if table is None:
                return False
        
        # use ending symbol to judge whether current word exist in our trie or not
        return ( '@' in table )
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        def helper( char, table):
            
            if char in table:
                return table[char]
            else:
                return None
            
        # -----------------------
        
        # check the prefix exist in trie or not
        table = self.trie
        
        for char in prefix:
            table = helper( char, table)
            
            if table is None:
                return False
        
        return True

    
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



def test_bench():

    trie = Trie();

    trie.insert("apple")
    print( trie.search("apple") )       # returns true
    print( trie.search("app") )         # returns false
    print( trie.startsWith("app") )     # returns true
    trie.insert("app")   
    print( trie.search("app") )         # returns true



if __name__ == "__main__":

    test_bench()
