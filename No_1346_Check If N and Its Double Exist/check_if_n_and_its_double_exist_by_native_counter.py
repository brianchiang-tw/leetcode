'''

Description:

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.



Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.



Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
 

Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3

'''



from collections import Counter
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        # dictionary:
        # key   : number
        # value : occurrence of number
        number_occ_dict = Counter(arr)
        
        for num in number_occ_dict:
            
            if num != 0:
                if 2*num in number_occ_dict:
                    return True
            
            else:
                # description demands i =/= j , A[i] = 2 * A[j]
                if number_occ_dict[0] >= 2:
                    return True
            
        return False



# n : the length of input array, arr.

## Time Complexity: O( n )
# 
# The overhead in time is the dictionary building and the for loop, which are of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, number_occ_dict, which is of O( n ).


def test_bench():

    test_data = [
                    [10,2,5,3],
                    [7,1,14,11],
                    [3,1,7,11],
                    [0,1,3,5,9]
                ]

    # expected output:
    '''
    True
    True
    False
    False    
    '''

    for sequence in test_data:

        print( Solution().checkIfExist(sequence) )

    return



if __name__ == '__main__':

    test_bench()