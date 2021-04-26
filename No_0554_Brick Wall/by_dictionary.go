/*

Description:

There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Example 1:


Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2



Example 2:

Input: wall = [[1],[1],[1]]
Output: 3
 

Constraints:

n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
sum(wall[i]) is the same for each row i.
1 <= wall[i][j] <= 231 - 1


*/

package No_0554

func Max(x, y int) int{
    if x > y {
        return x
    }
    return y
}

func leastBricks(wall [][]int) int {
    
    //// dictioanry
    // key: bounday
    // value: occurrence of boundary
    
    boundaryOccDict := make(map[int]int)
    
    brickRows := len(wall)
    
    // scan each brick row
    for _, curBrickRow := range wall{
        
        // reset current boundary to zero for each row
        curBoundary := 0
        
        // update boundary into dictionary
        // Take care that final boundary is excluded to satisfy definition
        for _, curBrickLength := range curBrickRow[:len(curBrickRow)-1]{
            
            curBoundary += curBrickLength
            
            boundaryOccDict[curBoundary] += 1
            
        }
        
    }
    
    // get occurrence of boundary
    maxBoundaryOccurrence := -1
    
    for _, curBoundaryOccurrence := range boundaryOccDict{
        maxBoundaryOccurrence = Max(maxBoundaryOccurrence, curBoundaryOccurrence)
    }
    
    // compute minimal crossing by occurrence of boundary
    minCrossing := 0
    
    if maxBoundaryOccurrence != -1{
        // general cases: mutiple bricks on each row
        minCrossing = brickRows - maxBoundaryOccurrence
        
    }else{
        // corner case: only one brick on each row
        minCrossing = brickRows
    }
    
    return minCrossing
}



// m : the height of brick wall
// n : the average of bricks on each row

//// Time Complexity: O( m * n )
//
// The overhead in time is the cost of iteration, which is of O( m * n )

//// Space Complexity: O( n )
//
// The overhead in space is the stroage of dictionary, which is of O( n )

// type "go test -v" in console to run uniitest