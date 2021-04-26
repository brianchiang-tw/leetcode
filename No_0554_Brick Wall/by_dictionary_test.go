package No_0554

import (
	"testing"
)

func TestCase1(t *testing.T) {
	var (
		wall     [][]int = [][]int{{1, 2, 2, 1}, {3, 1, 2}, {1, 3, 2}, {2, 4}, {3, 1, 2}}
		expected int     = 2
	)

	result := leastBricks(wall)

	if result != expected {
		t.Errorf("\n Wrnong answer. Expected = %v, Result = %v \n", expected, result)
	}

}

func TestCase2(t *testing.T) {
	var (
		wall     [][]int = [][]int{{1}, {1}, {1}}
		expected int     = 3
	)

	result := leastBricks(wall)

	if result != expected {
		t.Errorf("\n Wrnong answer. Expected = %v, Result = %v \n", expected, result)
	}

}
