'''

Description:

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''


from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # dictionary:
        # key   : character
        # value : occurrence of character
        source_dict = Counter(magazine)
        note_dict = Counter(ransomNote)
        
        
        # If char is not enough in magazie, return False
        for char in note_dict:
            if char not in source_dict or note_dict[char] > source_dict[char]:
                return False
        
        return True



# m : the character length of ransom note
# n : the character length of magazine

## Time Complexity: O( m + n )
#
# The overhead in time is the cost of dictionary building, which is of O( m + n ).

## Space Complexity: O( m + n )
#
# The overhead in space is the storage for dictionary, which is of O( m + n ).



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'a b')

def test_bench():

    test_data = [
                    TestEntry( a = "a", b = "b"),
                    TestEntry( a = "aa", b = "ab"),
                    TestEntry( a = "aa", b = "aab"),
                ]

    # expected output:
    '''
    False
    False
    True
    '''


    for t in test_data:

        print( Solution().canConstruct( ransomNote = t.a, magazine = t.b ) )
    
    return



if __name__ == '__main__':

    test_bench()

