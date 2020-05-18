'''

Description:

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").



Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

Hint #1  
Obviously, brute force will result in TLE. Think of something else.

Hint #2  
How will you check whether one string is a permutation of another string?

Hint #3  
One way is to sort the string and then compare. But, Is there a better way?

Hint #4  
If one string is a permutation of another string then they must one common metric. What is that?

Hint #5  
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?

Hint #6  
What about hash table? An array of size 26?


'''



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        size_1, size_2 = len(s1), len(s2)
        
        if ( size_1 > size_2 ) or ( size_1 * size_2 == 0 ):
            
            # Quick rejection for oversize pattern or empty input string 
            
            return False
        
        
        target_signature = sum( map(hash, s1) )
        
        cur_signature = sum( map(hash, s2[:size_1] ) )
        
        for tail_index in range(size_1, size_2 ):
            
            if cur_signature == target_signature:
                # Accept, find one match
                return True
            
            head_index = tail_index - size_1
            
            # update cur_signature for next iteration
            prev_char, next_char = s2[head_index], s2[tail_index]
            cur_signature += ( hash(next_char) - hash(prev_char) )

            
        if cur_signature == target_signature:
            # last comparison after iteraion is completed
            # Accept,find one match
            return True    
        
        else:
            # Reject, no match between s1 and s2
            return False



from collections import namedtuple
TestEntry = namedtuple('TestEntry', 's1 s2')

def test_bench():

    test_data = [
                    TestEntry( s1 = "ab", s2 = "eidbaooo" ),
                    TestEntry( s1 = "ab", s2 = "eidboaoo" ),
                ]

    # expected output:
    '''
    True
    False
    '''

    for t in test_data:

        print( Solution().checkInclusion( *t ) )
    
    return



if __name__ == '__main__':

    test_bench()    