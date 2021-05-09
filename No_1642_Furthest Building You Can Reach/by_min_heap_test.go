package No_1642

import (
	"testing"
)

func TestCase1(t *testing.T) {

	var (
		heights  []int = []int{4, 2, 7, 6, 9, 14, 12}
		bricks   int   = 5
		ladders  int   = 1
		expected int   = 4
	)

	result := furthestBuilding(heights, bricks, ladders)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v \n", expected, result)
	}

}

func TestCase2(t *testing.T) {

	var (
		heights  []int = []int{4, 12, 2, 7, 3, 18, 20, 3, 19}
		bricks   int   = 10
		ladders  int   = 2
		expected int   = 7
	)

	result := furthestBuilding(heights, bricks, ladders)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v \n", expected, result)
	}

}

func TestCase3(t *testing.T) {

	var (
		heights  []int = []int{14, 3, 19, 3}
		bricks   int   = 17
		ladders  int   = 0
		expected int   = 3
	)

	result := furthestBuilding(heights, bricks, ladders)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v \n", expected, result)
	}

}
