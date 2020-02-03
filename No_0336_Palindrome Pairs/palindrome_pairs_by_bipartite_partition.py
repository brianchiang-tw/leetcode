'''

Description:

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]



Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]

'''




from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        # dictionary by comprehension
        # key   : word
        # vluae : index of word
        word_index_dict = { word:index for index, word in enumerate(words) }
        
        # use set's property to avoid repeated pairs
        index_of_palindrome_pair = set()
        
        # check each word and its possible palindrome combination
        for index, word in enumerate(words):
            
            for i in range(0,len(word)+1, +1):
                
                # Make a bipartite partition with index i
                # word = left + right
                left    = word[:i]
                right   = word[i:]
                
                
                # If left is palindrome, and revrse of right exists,
                # then right[::-1] + left + right = right[::-1] + word is also a palindrome
                if left == left[::-1] and word_index_dict.get( right[::-1], -1) not in (index, -1):
                    index_of_palindrome_pair.add( (word_index_dict[ right[::-1] ], index ) )
                    
                    
                # If right is palindrome, and reverse of left exists,
                # then left + right + left[::-1] = word + left[::-1] is also a palindrome.
                if right == right[::-1] and word_index_dict.get( left[::-1], -1) not in (index, -1):
                    index_of_palindrome_pair.add( (index, word_index_dict[ left[::-1] ] ) )
        
        
        # convert set of tuple to list of list as final result
        result = list( map (list, index_of_palindrome_pair) )
        
        return result
                


# n : the length of input string array, words.
# k : the average character length of each word in input array.


## Time Complexity: O( n * k^2 )
#
# The overhead in time is the outer for loop iterating on (index, word), which is of O( n ), and
# the inner for loop iterating on i, which is of O( k ), and
# the word slicing operation word[:i] as well as word[i:], which is of O( k ).
# It takes O( n * k^2 ) totally


## Space Complexity: O( n )
#
# The overhead in space is the storage to maintain dictionary, word_index_dict, which is of O( n)

                
def test_bench():

    test_data = [
                    ["abcd","dcba","lls","s","sssll"],
                    ["bat","tab","cat"]
                ]

    # expected output:
    '''
    [[0, 1], [1, 0], [3, 2], [2, 4]]
    [[0, 1], [1, 0]]
    '''

    for string_array in test_data:

        print( Solution().palindromePairs(string_array) )
    
    return



if __name__ == '__main__':

    test_bench()
        