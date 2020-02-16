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


from collections import Counter

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        num_occ_dict = Counter(arr)
        
        threshold = len(arr) // 4
        
        
        for num in num_occ_dict:
            
            if num_occ_dict[num] > threshold:
                return num



# n : the length of input array, arr.
# k : the number of unique elements in array arr.

## Time Complexity: O(n)
#
# The overhead in time is the for loop, iterating on num, 
# and dictionary building of num_occ_dict, which are of O( n ).

## Space Complexity: O( k )
#
# THe overhead in space is the storage for dictinary, num_occ_dict, which is of O( k ).


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