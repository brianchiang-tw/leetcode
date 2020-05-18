'''

Description:

Given a sentence text (A sentence is a string of space-separated words) in the following format:

First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.

 

Example 1:

Input: text = "Leetcode is cool"
Output: "Is cool leetcode"
Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.



Example 2:

Input: text = "Keep calm and code on"
Output: "On and keep calm code"
Explanation: Output is ordered as follows:
"On" 2 letters.
"and" 3 letters.
"keep" 4 letters in case of tie order by position in original text.
"calm" 4 letters.
"code" 4 letters.



Example 3:

Input: text = "To be or not to be"
Output: "To be or to be not"
 

Constraints:

text begins with a capital letter and then contains lowercase letters and single space between words.
1 <= text.length <= 10^5

'''



class Solution:
    def arrangeWords(self, text: str) -> str:
        
        # Split each word by white space, store them in list
        words = [ *text.split() ]
        
        # Convert first word to lower case
        words[0] = words[0].lower()
        
        # Sort words by character length
        words.sort( key = len )
        
        # Convert back to string, separated by space
        # Then capitalize the result
        return ( ' '.join( words ) ).capitalize()



def test_bench():

    # expected output is in the comment

    test_data = [
                    "Leetcode is cool",         # Is cool leetcode
                    "Keep calm and code on",    # On and keep calm code
                    "To be or not to be",       # To be or to be not
                ]

    for test_string in test_data:

        print( Solution().arrangeWords( text = test_string ) )
    
    return



if __name__ == '__main__':

    test_bench()
