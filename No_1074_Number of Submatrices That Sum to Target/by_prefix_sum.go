/*

Description:

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.



Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.



Example 3:

Input: matrix = [[904]], target = 0
Output: 0
 

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8

*/

package No_1074

func numSubmatrixSumTarget(matrix [][]int, target int) int {
    
    // height and width of matrix
    h, w := len(matrix), len(matrix[0])
    
    // update prefix sum on each row
    for y := 0 ; y < h ; y++{
        for x:= 1 ; x < w; x++{
            matrix[y][x] = matrix[y][x] + matrix[y][x-1]
        }
    }
    
    // number of submatrices that sum to target
    counter := 0
    
    // sliding windows on x-axis, in range[left, right]
    for left := 0 ; left < w ; left ++{
        for right := left ; right < w ; right++{
            
            // accumulation for area so far
            accumulation := map[int]int{ 0 : 1}
            
            // area of current submatrices, bounded by [left, right] with height y
            area := 0
            
            // scan each possible height on y-axis
            for y := 0 ; y < h ; y++{
                
                if left > 0 {
                    area += matrix[y][right] - matrix[y][left-1]
                }else{
                    area += matrix[y][right]
                }
                
                // if ( area - target ) exists, then target must exist in submatrices
                counter += accumulation[ (area - target) ]
                
                // update dictionary with current accumulation area
                accumulation[area] += 1
                
            }
            
        }//end of right loop
        
    }//end of left loop
    
    return counter
    
}


// w : width of input matrix
// h : height of input matrix

//// Time Complexity: O( w^2 * h )
//
// The overhead in time is the cost of iteration, which is of O( w^2 * h )

//// Space Complexity: O( w * h )
//
// The overhead in space is the storage for dictionary, which is of O( w * h )

