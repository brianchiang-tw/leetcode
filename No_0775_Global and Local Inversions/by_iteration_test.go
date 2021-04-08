package No_0775

import (
	"testing"
)

func TestCase1( t *testing.T){
	var(
		A []int = []int{1, 0, 2}
		expected bool = true
	)

	result := isIdealPermutation(A)

	if result != expected {
		t.Errorf("Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}



func TestCase2( t *testing.T){
	var(
		A []int = []int{1, 2, 0}
		expected bool = false
	)

	result := isIdealPermutation(A)

	if result != expected {
		t.Errorf("Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}