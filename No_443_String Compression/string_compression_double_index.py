'''

Description:

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

'''

from typing import List

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        read_index, write_index = 0, 0
        
        while read_index < len( chars ):
            
            leading_char, len_of_cluster = chars[ read_index ], 0
            
            
            # read cluster of the same character
            while read_index < len( chars) and chars[ read_index ] == leading_char  :
                read_index, len_of_cluster = read_index+1, len_of_cluster + 1
            
            # write leading character of cluster
            chars[ write_index ], write_index = leading_char, write_index + 1
            
            # write length of cluster if length > 1
            if len_of_cluster > 1:
                for char_of_len in str(len_of_cluster):
                    chars[ write_index ], write_index = char_of_len, write_index + 1
            

        
        return write_index

# N : length of input list
# k : max of length of clutsters

## Time Complexity: O( N )
#
# The overhead is the outer while loop over read_index of O( N - k ), and inner while loop over read_index of O( k )
# The for loop for writing is O( 1 ) because of length of string is a constant of O( 1 )
# In summary, total time complexity is O( N )

## Space Complexity: O( 1 )
#
# The overhead is the index variable and temp variable to record leading character as well as length of cluster.




def test_bench():

    test_data = [ 
                    ["a","a","b","b","c","c","c"],
                    ["a","b","b","c","c","c"]

                ]

    # expected output:
    '''
    6
    5
    '''

    for t in test_data:

        print( Solution().compress(t) )

    return



if __name__ == '__main__':

    test_bench()