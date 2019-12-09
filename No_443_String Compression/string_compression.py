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

class Solution:
    def compress(self, chars: List[str]) -> int:

        # Note:
        # Description asks us to operate in-place, so creating new list to store result is Not allowed
    
        # add one spcial symbol '!' as ending character
        chars.append('!')
            
        leading_char, cur_char = None, None
        len_cluster, size = 0, len(chars)
        
        index_of_cluster = 0
        
        
        if len(chars) == 1 and chars[0] =='!':
            # corner case handling for input chars is empty string
            
            chars.pop()
            return 0
        
        
        for i in range(size):
            
            cur_char = chars[i]
            
            if 0 == i:
                    # Initial at index 0
                leading_char = chars[i]
                len_cluster = 1
                            
            else:
                
                if cur_char == leading_char:
                    # current character is the same as leading char
                    # keep going, and increase length of cluster by 1
                    len_cluster += 1
                    
                else:
                    # cluster hanlding


                    if len_cluster == 1:
                        
                            # updater leading char of current cluster in compress result
                        chars[index_of_cluster] = leading_char
                        
                            # no need to update length ( == 1), just let index_of_cluster move forwar
                        index_of_cluster += 1
                        
                            # update leading car as current char
                        leading_char = cur_char
                        
                            # reset cluster length to 1
                        len_cluster = 1
                        
                        
                    else:
                        
                            # updater leading char of current cluster in compress result
                        chars[index_of_cluster] = leading_char
                        

                            # need to update length ( != 1), placed next to leading_char
                            # Note: length(int) should convert to a list of characters from 0 ~ 9                   
                        len_str_list = list( str(len_cluster) )
                        for i in range(len(len_str_list)):
                            chars[ index_of_cluster + 1 + i ] = len_str_list[i]
                            
                        
                            # let index_of_cluster move forwar
                        index_of_cluster += 1 + len(len_str_list)
                        
                        
                            # update leading car as current char
                        leading_char = cur_char
                        

                            # reset cluster length to 1
                        len_cluster = 1
                        

            # return the length of compression string
        return index_of_cluster


# N : length of input list
# k : max of length of clutsters

## Time Complexity: O( N )
#
# The overhead is the outer while loop over i of O( N )
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