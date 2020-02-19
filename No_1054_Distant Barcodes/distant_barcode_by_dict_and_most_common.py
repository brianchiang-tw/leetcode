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
        
        index, size = 0, len(barcodes)
        
        # dictionary:
        # key   : number
        # value : occurrence of number
        num_occ_dict = Counter(barcodes)
        
        new_barcodes = [ 0 for i in range(size) ]
        
        for number, occ in num_occ_dict.most_common():
            
            for _ in range(occ):
                new_barcodes[index], index = number, index+2
                
                if index >= size:
                    index = 1
                    
        return new_barcodes






# n : the length of input array, barcodes
# k : total number of unique elements in input array.

## Time Complexity: O( n + k log k)
#
# The overhead in time is the for loop for rearrangement, which is up to O( n ) at most.
# And the cost of sorting dictionary, which is O( k log k )
#
# It takes O( n + k log k ) in total

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