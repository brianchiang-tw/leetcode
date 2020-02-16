'''

Description:

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5

'''



class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        threshold = len(arr) * 0.25
        
        prev, occurrence = -1, 0
        
        for num in arr:
            
            if num == prev :
                # current element is the same as previous one
                occurrence += 1

            else:
                # current element is different to previous one
                occurrence = 1
            
            
            if occurrence > threshold:
                # check the occurrence is over threshold or not
                return num
            
            
            # update previous element as current one
            prev = num



# n : the length of input array, arr.

## Time Complexity: O(n)
#
# The overhead in time is the for loop, iterating on num, which is of O( n ).

## Space Complexity: O( 1 )
#
# THe overhead in space is the storage for looping index and temporary variable, which is of O( 1 ).


def test_bench():

    test_data = [
                    [1,2,2,6,6,6,6,7,10],
                    [1,2,3,3,4,5,8,8,8]
                ]

    # expected output:
    '''
    6
    8
    '''

    for sequence in test_data:

        print( Solution().findSpecialInteger(sequence) )

    return 



if __name__ == '__main__':

    test_bench()