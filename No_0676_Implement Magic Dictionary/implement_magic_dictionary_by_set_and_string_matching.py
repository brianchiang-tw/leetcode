'''

Description:

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.

'''



from typing import List
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # a record of words
        self.word_set = set()
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        
        # add all words to word_set
        for word in dict:
            self.word_set.add(word)
        
        

        
    def is_only_one_diff(self, source: str, word:str) -> bool:
        
        if len(source) == len(word):
            # check if only one character differnece between source and word
            only_one_diffenece = False

            for i in range( len(source) ):
                if source[i] != word[i]:
                    
                    if not only_one_diffenece:
                        only_one_diffenece = True
                    else:
                        return False
            
            return only_one_diffenece
            
        else:
            # length is different
            # it is impossible to modify exactly one character to match source
            return False
        
        
        
    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        
        for source in self.word_set:
            
            if self.is_only_one_diff(source, word):
                return True
            
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)






# n : the length of input parameter, dict, in buildDict()
# k : the average length of input parameter, word, in search()


## Time Complexity: O( n * k )
#
# For buildDict():
# The overhead in time is the cost of set building of word_set, which is of O( n ).
#
# For search():
# The overhead in time os the cost of for loop iterating on source, which is of O( n ),
# and the cost of calling is_only_one_diff(), which is of O( k ).
#
# It takes O( n * k ) in total.

## Space Complexity: O( n )
#
# The overhead in space is the storage of word_set, which is of O( n ).



def test_bench():

    source_data = ["hello", "leetcode"] 
    query_data = ["hello", "hhllo", "hell", "leetcoded"]

    magic_dict = MagicDictionary()
    magic_dict.buildDict( source_data )

    # expected output:
    '''
    False
    True
    False
    False
    '''


    for query_word in query_data:
        print( magic_dict.search(query_word) )
    
    return 



if __name__ == '__main__':

    test_bench()
