
from typing import List
class Solution:
    
    
    def findNumbers(self, nums: List[int]) -> int:
        
        # convert all number to string, store in list
        strnum_list = list( map( str, nums) )
        
        # a functor to judge if a string is with even number digits
        func_even_digits = lambda x: (len(x)%2==0)
        
        # use functor to select those strings with even number digits
        list_even_num_of_digits =  list( filter( func_even_digits,  strnum_list) )
        
        # total count of even digits number
        return len( list_even_num_of_digits )
        



# n : the number of elements in input list

## Time Complexity: O(n)
#
# The overhead in time is the hidden iteraion of O( n ) in map... and list constructor.

## Space Complexity: O(n)
#
# The overhead in space is to maintain a string list of order O( n )



def test_bench():

    test_data = [12,345,2,6,7896]

    

    print( Solution().findNumbers(test_data) )

    return



if __name__ == '__main__':

    test_bench()