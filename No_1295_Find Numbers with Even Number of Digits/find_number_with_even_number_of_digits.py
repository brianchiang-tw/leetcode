
from typing import List
class Solution:
    
    
    def findNumbers(self, nums: List[int]) -> int:
        
        strnum_list = list( map( str, nums) )

        list_even_num_of_digits =  list( filter( lambda x: (len(x)%2==0),  strnum_list) )
        
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