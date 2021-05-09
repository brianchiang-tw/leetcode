package No_0063

import(
	"testing"
)

func TestCase1( t *testing.T){
	var(
		obstacleGrid [][]int = [][]int{{0,0,0},{0,1,0},{0,0,0}}
		expected int = 2
	)

	result := uniquePathsWithObstacles(obstacleGrid)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v", expected, result)
	}

}

func TestCase2( t *testing.T){
	var(
		obstacleGrid [][]int = [][]int{{0,1},{0,0}}
		expected int = 1
	)

	result := uniquePathsWithObstacles(obstacleGrid)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v", expected, result)
	}

}