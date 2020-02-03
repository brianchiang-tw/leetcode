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
        # 0 means the word is not reversed, 1 means the word is reversed
        words, length, result = sorted([(w, 0, i, len(w)) for i, w in enumerate(words)] +
                                       [(w[::-1], 1, i, len(w)) for i, w in enumerate(words)]), len(words) * 2, []
        
        #print(words)
        
        for i, (word1, rev1, ind1, len1) in enumerate(words):
            
            for j in range(i + 1, length):
                
                word2, rev2, ind2, _ = words[j]
                
                if word2.startswith(word1):
                    
                    if ind1 != ind2 and rev1 ^ rev2:
                        
                        rest = word2[len1:]
                        
                        if rest == rest[::-1]: result += ([ind1, ind2],) if rev2 else ([ind2, ind1],)
                            
                else:
                    break
                    
        return result
                
                
                
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
                        
                
                
        