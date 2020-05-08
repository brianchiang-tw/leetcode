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



Hint #1  

Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].



Hint #2  
On each step of the loop check if we have seen the element 2 * arr[i] so far or arr[i] / 2 was seen if arr[i] % 2 == 0.

'''



from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        num_idx_dict = {}
        
        for idx, number in enumerate(arr):
            
            if number:
                # general handle for non-zero number
                if 2*number in num_idx_dict:
                    return True
            
                elif number/2 in num_idx_dict:
                    return True
                
            elif number in num_idx_dict:
                # special handle for zero
                return True
            
            
            num_idx_dict[ number ] = idx
                
        return False



# n : the length of input array, arr.

## Time Complexity: O( n )
#
# The overhead in time is the cost of linear scan, which is of O( n ).

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'sequence')

def test_bench():

    test_data = [
                    TestEntry( sequence = [10,2,5,3] ),
                    TestEntry( sequence =  [7,1,14,11] ),
                    TestEntry( sequence =  [3,1,7,11] ),
                    TestEntry( sequence =  [0,1,5] ),
                    TestEntry( sequence =  [0,1,5,3] ),
                ]        

    # expected output:
    '''
    True
    True
    False
    False
    False
    '''


    for t in test_data:

        print( Solution().checkIfExist( arr = t.sequence) )
    
    return



if __name__ == '__main__':

    test_bench()