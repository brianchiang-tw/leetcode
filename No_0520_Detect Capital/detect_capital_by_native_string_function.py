'''

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 


Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

'''



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # if it is a capital word, or of all upper-case letters already
        flag_capital = word.istitle() or word.isupper()
        
        #if it is of all lower-case letters already
        flag_all_lower_case = word.islower()
        
        if flag_capital or flag_all_lower_case:    
            # Accept:
            return True
        
        else:
            # Reject:
            # this word breaks the rule
            return False



# n : the length of input string


## Time Complexity: O( n )
#
# The overhead is time is the cost of checking on letters, which is of O( n ).


## Space Complexity: O( 1 )
#
# The overhead in space is the variable for flag, which is of O( 1 ).



def test_bench():

    test_data = [
                    "USA",
                    "Flag",
                    "FlaG",
                    "Dog",
                    "DOG",
                    "dog",
                    "dOg"
                ]

    # expected output:
    '''
    True
    True
    False
    True
    True
    True
    False    
    '''

    for test_string in test_data:

        print( Solution().detectCapitalUse(test_string) )
    
    return 



if __name__ == '__main__':

    test_bench()