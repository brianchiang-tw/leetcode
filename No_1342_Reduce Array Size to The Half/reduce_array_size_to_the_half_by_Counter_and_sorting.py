'''

Description:

Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.



Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.



Example 3:

Input: arr = [1,9]
Output: 1



Example 4:

Input: arr = [1000,1000,3,7]
Output: 1



Example 5:

Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5
 

Constraints:

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5

'''



from typing import List
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        # dictionary:
        # key   : number
        # value : occurrence
        num_occ_dict = Counter(arr)
        
        # get the length of input array
        size = len(arr)
        
        # keep occurrences in descending order
        occurrences = sorted( num_occ_dict.values(), reverse = True )
        
        
        removal_op_counter, removal_size = 0, 0
        
        # keep removing number until half size is met
        while removal_size < (size+1)//2:
        
            removal_size += occurrences[removal_op_counter]
            removal_op_counter += 1
        
        return removal_op_counter



# n : the length of input array, arr.
# k : the number of unique element in input array, arr.

## Time Complexity: O( n + k log k)
#
# The overhead in time is the cost to build dictionary of O( n ), and
# to sort the occurrence of O( k log k )


## Space Complexity: O( k )
#
# The overhead in space is the storage to keep num_occ_dict, and occurrences, which are of O( k )

def test_bench():

    test_data = [
                    [3,3,3,3,5,5,5,2,2,7],
                    [7,7,7,7,7,7],
                    [1,9],
                    [1000,1000,3,7],
                    [1,2,3,4,5,6,7,8,9,10]
                ]


    for sequence in test_data:

        print( Solution().minSetSize(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()