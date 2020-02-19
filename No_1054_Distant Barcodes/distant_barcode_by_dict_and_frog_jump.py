'''

Description:

In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]



Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 

Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
 

'''



from collections import Counter
from typing import List
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        size = len(barcodes)
        
        # dictionary:
        # key   : number
        # value : occurrence of number
        num_occ_dict = Counter(barcodes)
        
        new_barcodes = [ 0 for i in range(size) ]
        
        fill_counter = 0
        fill_index = 0
        
        num_of_max_occ, max_occ = num_occ_dict.most_common(1)[0]
        
        # Step_1: Rearrange number with highest occurrence, by frog jump with one space
        for _ in range(max_occ):
            new_barcodes[fill_index] = num_of_max_occ
            fill_index += 2
            
        del num_occ_dict[num_of_max_occ]
        
        
        # Step_#2: Rearrange other numbers, by frog jump with one space
        if fill_index >= size:
            fill_index = 1
            
        for num in num_occ_dict.keys():
            
            for _ in range( num_occ_dict[num] ):
                new_barcodes[fill_index] = num
                fill_index += 2
                
                if fill_index >= size:
                    fill_index = 1
                    
        return new_barcodes



# n : the length of input array, barcodes

## Time Complexity: O( n )
#
# The overhead in time is the for loop for rearrangement, which is up to O( n ) at most.

## Space Complexity: O( n )
#
# The overhead in space is the storage for dictionary, num_occ_dict, which is of O( n ).


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'barcode')
def test_bench():

    test_data = [
                    TestEntry([1,1,1,2,2,2]),
                    TestEntry([1,1,1,1,2,2,3,3])
                ]

    # expected output:
    # Note: There are multiple acceptable solutions.
    '''
    [1, 2, 1, 2, 1, 2]
    [1, 2, 1, 2, 1, 3, 1, 3]
    '''

    for t in test_data:
        print(Solution().rearrangeBarcodes( t.barcode) )

    return 



if __name__ == '__main__':

    test_bench()