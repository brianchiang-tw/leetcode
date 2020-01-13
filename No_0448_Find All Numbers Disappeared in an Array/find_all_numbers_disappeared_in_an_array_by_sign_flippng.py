'''

Description:

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

'''



from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        for number in nums:
            
            present_indx = abs(number)-1
            if nums[present_indx] > 0 :
                # use negative sign to mark number is presented in array
                nums[present_indx] = -nums[present_indx]
            else:
                pass
            
        disappeared_num = []
        
        for index,x in enumerate(nums):
            
            # the disappeared numbers are those grids which are still with positive value
            if x > 0:
                disappeared_num.append( index+1 )
        
        return disappeared_num



def test_bench():

    test_data = [
                    [4, 3, 2, 7, 8, 2, 3, 1],
                    [1, 1, 2, 2, 3],
                    [1, 3, 3, 4, 3]
                ]

    for sequence in test_data:

        print( Solution().findDisappearedNumbers(sequence) )

    return 



if __name__ == '__main__':

    test_bench()