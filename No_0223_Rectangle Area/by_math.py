'''

Description:

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.



'''



class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        left_boundary = max(A, E)
        right_boundary = min(C, G)
        
        top_boundary = min(D, H)
        bottom_bondary = max(B, F)
        
        
        area_1 = (C - A)*(D - B)
        area_2 = (G - E)*(H - F)
        
        if (left_boundary < right_boundary) and (bottom_bondary < top_boundary):
            # area_1 and area_2 has overlapped area
            intersection = ( right_boundary - left_boundary ) * ( top_boundary - bottom_bondary )
        else:
            # area_1 and area_2 has no overlapped area
            intersection = 0
        
        return area_1 + area_2 - intersection



## Time Complexity: O( 1 )
#
# The overhead in time is the cost of computation of boundary and area, which is of O( 1 )

## Space Complexity: O( 1 )
#
# The overhead in space is the storage for temporary variable, which is of O( 1 )



def test_bench():

    test_data = {'A' : -3, 'B' : 0, 'C' : 3, 'D' : 4, 'E' : 0, 'F' : -1, 'G' : 9, 'H' : 2}

    # expected output:
    # 45
    print( Solution().computeArea(**test_data) )

    test_data = { 'A': -2, 'B': -2, 'C': 2, 'D': 2, 'E': 3, 'F': 3, 'G':4, 'H': 4 }

    # expected output:
    # 17
    print( Solution().computeArea(**test_data) )


    return



if __name__ == '__main__':

    test_bench()