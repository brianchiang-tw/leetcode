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
        
        
        # helper to judge s is palindrome or not
        def is_palindrome( s: str):

            if s == '':
                return False
            
            i, j = 0, len(s)-1

            while i < j:

                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1

            return True
        
        
        # key   : word
        # value : index of word in list
        word_index_dict = { word: index for index,word in enumerate(words) }
        

        
        # a storage for output
        index_of_palindrome_pair = set()
        
        
        # check each word
        for index, word in enumerate(words):
        
        
            if is_palindrome(word) and '' in word_index_dict:
                # Case_#1: 
                # If word is palindrome, then word + '' and '' + word are also palindromes.
                index_of_empty_string = word_index_dict['']
                index_of_palindrome_pair.add( (index, index_of_empty_string) )
                index_of_palindrome_pair.add( (index_of_empty_string, index) )
                
            
            reverse_word = word[::-1]
            
            
            if word != reverse_word and reverse_word in word_index_dict:
                # Case_#2
                # If word's reverse exists, then word + word[::-1] and word[::-1] + word are also palindromes.
                
                index_of_reverse_word = word_index_dict[reverse_word]
                index_of_palindrome_pair.add( (index, index_of_reverse_word) )
                index_of_palindrome_pair.add( (index_of_reverse_word, index) )
                
                
            
            for i in range(1, len(word)):
                # Case_#3
                # Let word = left + right
                
                # If left is palindrome and right[::-1] exists, 
                # then right[::-1] + left + right = right[::-1] + word is also palindrome.
                
                # If right is palindrome and left[::-1] exists, 
                # then left + right + left[::-1] = word + left[::-1] is also palindrome.
                
                left, left_rev      = word[:i], word[:i][::-1]
                right, right_rev    = word[i:], word[i:][::-1]
                
                if is_palindrome(left) and right_rev in word_index_dict:
                    index_of_reverse_word = word_index_dict[right_rev]
                    index_of_palindrome_pair.add( (index_of_reverse_word, index) )
                
                if is_palindrome(right) and left_rev in word_index_dict:
                    index_of_reverse_word = word_index_dict[left_rev]
                    index_of_palindrome_pair.add( (index, index_of_reverse_word) )
                
            
            
        return index_of_palindrome_pair
                
                
                
                


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
    {(0, 1), (1, 0), (3, 2), (2, 4)}
    {(0, 1), (1, 0)}
    '''

    for string_array in test_data:

        print( Solution().palindromePairs(string_array) )
    
    return



if __name__ == '__main__':

    test_bench()
        
                
                
                
        