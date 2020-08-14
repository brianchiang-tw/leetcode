'''

Description:

You should design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) adds word to the data structure, it can be matched later.
bool search(word) returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

'''



from collections import defaultdict

class Node:
    
    def __init__(self):
        
		# each character maps to one level in Trie
        self.trie = defaultdict(Node)
		
		# current level is a word or not
        self.is_word = False
        

class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        
        cur = self.root
        
        for char in word:
            cur = cur.trie[char]
        
        cur.is_word = True
    
    
    
    def match(self, word, index, node):
        
        if node is None:
			# current character does not exist in Trie
            return False
        
        elif index == len(word):
			# current level is the same as word's character length
			# check is_word flag
            return node.is_word
        
        if word[index] != '.':
			
			# try to match each character by DFS in Trie
            return node is not None and self.match(word, index+1, node.trie.get(word[index]))
        
        else:
			# handle for wildcard character matching
            for child_node in node.trie.values():
                if self.match(word, index+1, child_node):
                    return True
                
            return False
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        return self.match(word=word, index=0, node=self.root)



import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")

        result = wordDictionary.search("pad") # return False
        self.assertEqual(result, False)

        result = wordDictionary.search("bad") # return True
        self.assertEqual(result, True)

        result = wordDictionary.search(".ad") # return True
        self.assertEqual(result, True)

        result = wordDictionary.search("b..") # return True
        self.assertEqual(result, True)



if __name__ == '__main__':

    unittest.main()