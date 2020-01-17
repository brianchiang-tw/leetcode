'''

Description:

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]



Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
 

Note:

1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.

'''



from typing import List
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        # tokens split by whitespace characters
        tokens = list( text.split() )
        
        # storage for output
        word_after_bigram = []
        
        # scan each possible triple straight position
        # Note: take care the last valid index of i
        for i in range(len(tokens)-2 ):
            
            # check the words in order
            if tokens[i] == first and tokens[i+1] == second:
                
                # hit:
                # update third word to list
                word_after_bigram.append( tokens[i+2] )
                
        
        return word_after_bigram
                
# n : the number of tokens in input

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for third words, which is of O( n ).



def test_bench():

    test_data = [
                    ("alice is a good girl she is a good student", "a", "good"),
                    ("we will we will rock you", "we", "will"),
                ]


    # expected output:
    '''
    ['girl', 'student']
    ['we', 'rock']
    '''


    for test_string, first, second in test_data:

        print( Solution().findOcurrences(test_string, first, second) )
    
    return 



if __name__ == '__main__':

    test_bench()