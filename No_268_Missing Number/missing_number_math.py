from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # array containing n distinct numbers taken from 0, 1, 2, ..., n
        
        #   sum of ideal array without missing
        # = sum of array + missing element
        # = 0 + 1 + 2 + ... + missing element + ... + n 
        # = 0 + 1 + 2 + ... + n
        # = 1 + 2 + ... + n
        # = (1+n)*n // 2
        #
        # => sum of ideal array without missing - sum of array = missing element

        n = len(nums)
        
        missing_element = (1+n)*n // 2 - sum( nums ) 
        
        return missing_element



def test_bench():

    test_data = [
                    # missing 8
                    [9,6,4,2,3,5,7,0,1],

                    # missing 2
                    [3,0,1]
                ]


    # expected output:
    '''
    8
    2
    '''


    for series in test_data:

        print( Solution().missingNumber(series) )

    return


if __name__ == '__main__':

    test_bench()