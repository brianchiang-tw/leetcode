package No_0063

func uniquePathsWithObstacles(obstacleGrid [][]int) int {

	// helper function
	var allowToVisit func(x, y int) int

	allowToVisit = func(x, y int) int {
		// 1 : allow to visit
		// 0 : can not visit due to obstacle
		return 1 - obstacleGrid[y][x]
	}

	h, w := len(obstacleGrid), len(obstacleGrid[0])

	if h*w == 0 || allowToVisit(0, 0) == 0 {
		// Quick response for invalid cases
		return 0
	}

	// update [0][0] as start point with one valid path
	obstacleGrid[0][0] = 1

	// base case: leftmost column
	for y := 1; y < h; y++ {
		obstacleGrid[y][0] = obstacleGrid[y-1][0] * allowToVisit(0, y)
	}

	// base case: top column
	for x := 1; x < w; x++ {
		obstacleGrid[0][x] = obstacleGrid[0][x-1] * allowToVisit(x, 0)
	}

	// general cases:
	for y := 1; y < h; y++ {
		for x := 1; x < w; x++ {

			// update path count form left and top
			obstacleGrid[y][x] = (obstacleGrid[y][x-1] + obstacleGrid[y-1][x]) * allowToVisit(x, y)
		}
	}

	return obstacleGrid[h-1][w-1]
}


// m,n : dimension of rows and columns

//// Time Complexity: O( m * n )
//
// The overhead in time is the nested for loops iterating on (i, j), which is of O( m * n )



//// Space Complexity: O( 1 )
//
// The overhead in space is the storage for loop index and temporary varaible, which is of O( 1 )
