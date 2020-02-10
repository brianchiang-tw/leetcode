# This implementation is just a self-practice, not good enough to pass Online Judge due to high complexity in time.

from itertools import combinations
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        def valid_triangle( edge_triplet ):
            
            # a + b > c must be True for any two edge a, b in triangle
            
            if edge_triplet[0] + edge_triplet[1] <= edge_triplet[2]:
                return False
            
            if edge_triplet[1] + edge_triplet[2] <= edge_triplet[0]:
                return False
            
            if edge_triplet[0] + edge_triplet[2] <= edge_triplet[1]:
                return False
            
            return True
        
        
        triplets = combinations( nums, 3)
        
        return sum( [ 1 for t in triplets if valid_triangle(t) ] )
        


def test_bench():

    test_data = [ 
                    [2,2,3,4],
                    [4,3,2,2],
                    [3,3,4,5,6,6,7,8,10,9]
                ] 


    # expected output:
    '''
    3
    3
    86
    '''

    for sequence in test_data:

        print( Solution().triangleNumber(sequence))

    return



if __name__ == '__main__':

    test_bench()