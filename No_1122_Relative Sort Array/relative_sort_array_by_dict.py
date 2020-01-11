'''

Description:

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.

'''



from collections import Counter
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        # make a dictionary of arr1
        # key   : number
        # value : occurrence
        num_occ_dict = Counter( arr1 )
        
        overwrite_index = 0

        # reconstruct arr1 by arr2's relative order
        for ref_val in arr2:
            
            length = num_occ_dict[ref_val]
            arr1[ overwrite_index : overwrite_index+length ] = [ ref_val ]*length
            overwrite_index += length

            del num_occ_dict[ref_val]
        
        
        
        # reconstruct those numbers in arr1 but not in arr2
        remain_keys = list( num_occ_dict.keys() )
        remain_keys.sort()
        
        for other_num in remain_keys:
            
            length = num_occ_dict[other_num]
            arr1[ overwrite_index : overwrite_index+length ] = [ other_num ]*length
            overwrite_index += length
               
        return arr1



# m : the length of input list, arr1.
# n : the length of input list, arr2.
# r : the number of element is arr1 but not in arr2.

## Time Complexity: O( n + r log r )
#
# The overhead in time is the for loop iterating on ref_val, which if of O( n ), 
# and the time to sort remain_keys, which is of O( r log r ).
# It takes O( n + r log r ) in total.



## Space Complexity: O( m )
#
# The overhead in space is the storage for num_occ_dict, which is of O( n ).



def test_bench():

    test_data = [
                    ([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])
                ]

    # expected output:
    '''
    [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    '''

    for arr1, arr2 in test_data:

        print( Solution().relativeSortArray(arr1, arr2) )



if __name__ == '__main__':

    test_bench()