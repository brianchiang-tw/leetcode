'''

Description:

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

'''


class Solution:

    def reverseWords(self, s):
        
        # parse and get each string token
        tokens = list( map( str, s.split() ) )
        
        # reverse each string token
        for i in range( len(tokens) ):
            tokens[i] = tokens[i][::-1]
        
        print(tokens)

        # concatenate string token together, separated by one whitespace
        return ' '.join( tokens )


# n : the length of the input string

## Time Complexity: O( n )
#
# The overhead is the word split and word reverse, which is of O( n )


## Space Complexity: O( n )
#
# The overhead is the storage for reverse word, which is of the same length of input.
# Thus, it is O( n )



def test_bench():

    test_data = [
                    "Let's take LeetCode contest",
                    "Cats are so cute"
                ]

    # expected output:
    '''
    s'teL ekat edoCteeL tsetnoc
    staC era os etuc
    '''

    for test_str in test_data:

        print( Solution().reverseWords(test_str) )

    return 



if __name__ == '__main__':

    test_bench()