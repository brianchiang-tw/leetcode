'''

Description:

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.

'''


# This implementation is just for practice, not a good one in run-time.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        char_list = list(text)
        
        target = 'balloon'
        
        counter = 0
        while True:
            
            try:
                # make ballon with greedy apporach
                for char in target:
                    char_list.remove(char)
                    
            except ValueError:
                # text has no enough characters to make ballon
                return counter
            else:
                # current iteration success, increase counter by 1
                counter +=1