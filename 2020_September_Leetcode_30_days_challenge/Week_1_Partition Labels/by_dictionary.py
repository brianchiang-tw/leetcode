'''

Description:

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]


Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
 

'''


from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        char_last_pos = {}
        
        for idx, char in enumerate(S):
            
            # update latest position index for each character is S
            char_last_pos[char] = idx
        
        
        # ------------------------------------------------------------
        
        start, partition_length = 0, []
        last_position = 0
        
        # make partition based on lastest position index of characters
        for idx, char in enumerate(S):
            
			# update and maximize last position of character
            last_position = max(last_position, char_last_pos[char])
            
            if idx == last_position:
                
                # those characters from start to last_position forms a partition
                cur_partition_length = last_position - start + 1
                
                partition_length.append( cur_partition_length )
                
                # update start for next partition
                start = idx + 1
                
        
        return partition_length



# n : the character length of string, S

## Time Complexity: O( n )
#
# The overhead in time is the cost of iteration, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n )



import unittest

class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().partitionLabels( S="ababcbacadefegdehijhklij" )
        self.assertEqual(result, [9, 7, 8] )


    def test_case_2( self ):

        result = Solution().partitionLabels( S="baacdc" )
        self.assertEqual(result, [1, 2, 3] )


if __name__ == '__main__':

    unittest.main()
