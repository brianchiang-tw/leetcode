class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        # Corner case hanlding:
        # If nums is empty list, return insert position = 0
        if( len(nums) == 0 ):
            return 0
        
        
        # check existence of target
        if target in nums:
            # target is already in nums, return the index
            return nums.index( target )
        
        
        else:

            # target is a incoming new element
            
            min_element = nums[0]
            max_element = nums[-1]
            
            
            if target < min_element:
                # Base case :
                # If target is smaller than min element, return insert position = 0
                
                return 0
            
            
            elif target > max_element:
                # Base case :
                # If target is larger than max element, return insert position = length of nums
                
                return len(nums)
            
            else:
                # General case:
                
                # find the insert position by compariosn
                for i in range( len(nums) ):
                    
                    if nums[i] < target and nums[i+1] > target:
                        # catch the insertion index
                        return (i+1)
                    
                    else:
                        # keep finding appropriate index for insertion
                        pass
                        continue


# N : the length of nums = the number of input elements

## Time Compleixty:
# O( N )
#
#   For best case: 
# If target is not in nums, and it is smaller than minimum element or larger than maximum element
# direct return 0 or len(nums)
# It takes O( 1 ) to carry out comparison with min/max and return constant value.
#
#   For average case and worst case:
# If target is in nums, it takes O( N ) to find the index of itself.
# If target is not in nums, it takes O( N ) to find the appropiate index that keeps sorting order.

## Space Complexity
# O( 1 )
# This function only needs some variable to store min, max element as well as loop index i.



def test_bench():

    test_cases =    [  
                        ([1,3,5,6], 5),
                        ([1,3,5,6], 2),
                        ([1,3,5,6], 7),
                        ([1,3,5,6], 0)
                    ]


    for test_data in test_cases:

        insert_position = Solution().searchInsert( nums = test_data[0], target = test_data[1] )

        print( insert_position )



if __name__ == "__main__":

    test_bench()