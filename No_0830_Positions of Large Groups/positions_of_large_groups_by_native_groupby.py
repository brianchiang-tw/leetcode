'''

Description:

In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.



Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.



Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
 

Note:  1 <= S.length <= 1000

'''



from itertools import groupby
from typing import List
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        
        # a storage for output index pairs
        large_group_index = []
        
        # starting index initialized to the head
        cur_index = 0

        # cluster same characters into one group
        for key, group in groupby(S):
            
            # Note:
            # current group = list( group )
            
            # current size of current group
            size_of_cur_group = len( list(group) )

            
            # capture large groups with size >= 3
            if size_of_cur_group >= 3:
                large_group_index.append( [cur_index, cur_index+size_of_cur_group-1] )
        
            # update starting index
            cur_index += size_of_cur_group
         

        
        return large_group_index



# n : the length of input string, S.

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on (key, group), which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for output list, large_group_index, which is of O( n ).



def test_bench():

    test_data = [
                    "abbxxxxzzy",
                    "abc",
                    "abcdddeeeeaabbbcd"
                ]

    # expected output:
    '''
    [[3, 6]]
    []
    [[3, 5], [6, 9], [12, 14]]    
    '''


    for test_string in test_data :

        print( Solution().largeGroupPositions(test_string) )

    return



if __name__ == '__main__':

    test_bench()