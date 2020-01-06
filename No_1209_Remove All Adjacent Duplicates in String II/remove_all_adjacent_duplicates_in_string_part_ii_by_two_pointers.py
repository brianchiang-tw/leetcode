class Solution:
    
    def removeDuplicates(self, s: str, k: int) -> str:
    
        output_index = 0
        size = len(s)
        
        adj_len = [ 0 for i in range(size)]
        
        output_s = list( [ "" for i in range(size)] )
        
        
        for scan_index in range( size ):
        
            output_s[output_index] = s[scan_index]
        
            if output_index > 0 and output_s[output_index-1] == s[scan_index]:
                adj_len[output_index] = adj_len[output_index-1] + 1
            else:
                adj_len[output_index] = 1
                
            if adj_len[output_index] == k:
                # discard adjacnt duplicates with length k
                output_index -= k
            
            output_index += 1
        
        return ''.join(output_s)[0:output_index]



# n : the length of input s

## Time Complexity: O( n )
#
# The overhead in time is the for loop iterating on scan_index, which is of O( n )

## Space Complexity: O( n )
#
# The overhead in space is the storage for the output_s, which if of O( n )



def test_bench():

    test_data = [
                    ("abcd", 2),
                    ("deeedbbcccbdaa",3),
                    ("pbbcggttciiippooaais", 2)
                ]

    # expected output:
    '''
    abcd
    aa
    ps
    '''


    for test_str, k in test_data :

        print( Solution().removeDuplicates(test_str, k) )

    return 



if __name__ == '__main__':

    test_bench()