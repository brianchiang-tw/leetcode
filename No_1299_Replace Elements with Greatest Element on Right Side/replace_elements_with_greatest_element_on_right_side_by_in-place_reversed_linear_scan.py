'''

Description:

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

'''



from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        size = len(arr)
        right_hand_max = -1
        
        for i in range( size-1, -1, -1):
    
            arr[i], right_hand_max = right_hand_max, max( right_hand_max, arr[i])
        
        return arr



# n : the length of input array, arr

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on i, which is of O( n )

## Space Complexity: O( 1 )
#
# THe overhead in space is the storage looping and max-update variabel, which is of O( 1 )




def test_bench():

    test_data = [  
                    [17,18,5,4,6,1],
                    list( range(1,11) ),
                    list( range(10,0, -1) )
                ]

    # expected output:
    '''
    [18, 6, 6, 6, 1, -1]
    [10, 10, 10, 10, 10, 10, 10, 10, 10, -1]
    [9, 8, 7, 6, 5, 4, 3, 2, 1, -1]
    '''


    for sequence in test_data:

        print( Solution().replaceElements(sequence) )
    
    return 



if __name__ == '__main__':

    test_bench()