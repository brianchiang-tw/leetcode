package No_0923

import (
	"testing"
)

func TestCase1(t *testing.T) {
	var (
		arr          = []int{1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
		target   int = 8
		expected int = 20
	)
	result := threeSumMulti(arr, target)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v  Result = %v", expected, result)
	}
}

func TestCase2(t *testing.T) {
	var (
		arr          = []int{1, 1, 2, 2, 2, 2}
		target   int = 5
		expected int = 12
	)
	result := threeSumMulti(arr, target)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v  Result = %v", expected, result)
	}
}
