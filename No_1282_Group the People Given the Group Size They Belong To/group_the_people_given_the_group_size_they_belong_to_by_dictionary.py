'''

Description:

There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the array groupSizes of length n telling the group size each person belongs to, return the groups there are and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there exists at least one solution. 

 

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].



Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
 

Constraints:

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n

'''



from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        # to record all the grouping of each group size
        gSize_memeber_dict = defaultdict(list)
        
        # temporarily buffer for grouping
        temp_dict = defaultdict(list)
        
        for person_id, grp_size in enumerate(groupSizes):
        
            temp_dict[grp_size].append( person_id )
        
            # If group size is met, 
            # then appeend to gSize_memeber_dict,
            # and clear temp dict[grp_size]
            if len(temp_dict[grp_size]) == grp_size:
                
                gSize_memeber_dict[grp_size].append( temp_dict[grp_size][::] )
                
                temp_dict[grp_size].clear()
        
        
        return [ grouping for size in gSize_memeber_dict for grouping in gSize_memeber_dict[size] ]



# n : the length of input array, groupSizes.

## Time Complexity: O( n )
#
# The overhead in time is the for loop, iterating on (person_id, grp_size), which is of O( n ).



## Space Complexity: O( n )
#
# The overhead in space is the storge for output list comprehension, which is of O( n ).



def test_bench():
    
    test_data = [
                    [3,3,3,3,3,1,3],
                    [2,1,3,3,3,2]
                ]

    # expected output:
    # Note: There are many valid solutions to each input. Please refer to description.
    '''
    [[0, 1, 2], [3, 4, 6], [5]]
    [[1], [2, 3, 4], [0, 5]]    
    '''

    for group_sizes in test_data:

        print( Solution().groupThePeople(group_sizes) )
    
    return 



if __name__ == '__main__':

    test_bench()