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



from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        # key   : charachter
        # value : occurrence of character
        char_occ_dict = Counter('balloon')
        
        # 10**4 is maximal length of text, given by description
        minimal_num_of_copies = 10**4 + 1
        
        # visit each character in dictionary of balloon, and
        # update minimal number of copies
        for char_key, char_occ in char_occ_dict.items():
            minimal_num_of_copies = min( minimal_num_of_copies, text.count(char_key) // char_occ )
        
        return minimal_num_of_copies



# n : the length of input string, text.

## Time Complexity: O( n )
#
# Although there is a for loop iterating on (char_key, char_occ), its itertaion is fixed of 5 times.
# The real overhead in time is the calling of text.count(char_key), which is of O( n )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for dictionary, char_occ_dict, which is of O( 1 ).


def test_bench():

    test_data = [
                    "nlaebolko",
                    "loonbalxballpoon",
                    "leetcode"
                ]

    # expected output:
    '''
    1
    2
    0
    '''

    for test_string in test_data:

        print( Solution().maxNumberOfBalloons(test_string) )

    return 



if __name__ == '__main__':

    test_bench()