'''

Description:

Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"



Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"



Example 3:

Input: nums = [1]
Output: "1"



Example 4:

Input: nums = [10]
Output: "10"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109

'''



class Solution:
    
    def largestNumber(self, nums):
        
        nums = self.mergeSort(nums, 0, len(nums)-1)
        
        return str(int("".join(map(str, nums))))

    def compare(self, s1, s2):
        
        # comparison between two string
        return str(s1) + str(s2) > str(s2) + str(s1)        
    
    def mergeSort(self, nums, l, r):
        
        if l > r:
            # base case, no string
            return 
        
        if l == r:
            # single string
            return [nums[l]]
        
        # general case
        mid = l + (r-l)//2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid+1, r)
        
        return self.merge(left, right)

    
    
    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        
        while i < len(l1) and j < len(l2):
            
            if not self.compare(l1[i], l2[j]):
                res.append(l2[j])
                j += 1
                
            else:
                res.append(l1[i])
                i += 1
        
        
        res.extend(l1[i:] or l2[j:])
        
        return res        


# n : the length of nums

## Time Complexity: O( n log n )
#
# The overhead in time is the cost of merge sort, which is of O( n log n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for res, which is of O( n )


import unittest
class Testing( unittest.TestCase ):

    def test_case_1( self ):

        result = Solution().largestNumber( nums=[10,2] )
        self.assertEqual(result, "210")


    def test_case_2( self ):

        result = Solution().largestNumber( nums= [3,30,34,5,9] )
        self.assertEqual(result, "9534330")


    def test_case_3( self ):

        result = Solution().largestNumber( nums= [1] )
        self.assertEqual(result, "1")


    def test_case_4( self ):

        result = Solution().largestNumber( nums= [10] )
        self.assertEqual(result, "10")




if __name__ == '__main__':

    unittest.main()        