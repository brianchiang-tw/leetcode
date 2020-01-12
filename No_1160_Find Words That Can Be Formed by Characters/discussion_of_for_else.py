from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
          
        list_of_success = []
        
        # visit each word
        for word in words:
            
            loop_complete_without_early_break = True
            # check each character
            for character in word:
                
                if word.count( character ) > chars.count( character ):
                    # miss:
                    # chars has no enough characters to make the word
                    loop_complete_without_early_break = False
                    break
                    
            
            if loop_complete_without_early_break:
                # hit:
                # add the word into list of success
                list_of_success.append( word )
                
                
        return len ( ''.join( list_of_success) )



# m : the length of input list, words.
# n : the maximal length of word in words

## Time Complexity : O( m * n )
#
# The overhead in time is the nested for loops iterating on (word, character), which is of O( m * n )

## Space Complexity : O( m * n )
#
# The overhead in space is the storage for list_of_success, which is of O( m * n )



def test_bench():

    test_data = [
                    (["cat","bt","hat","tree"], "atach"),
                    (["hello","world","leetcode"], "welldonehoneyr")
                ]

    # expected output:
    '''
    6
    10
    '''

    for words, chars in test_data:

        print( Solution().countCharacters(words, chars) )

    return 



if __name__ == '__main__':

    test_bench()