package No_0326

import (
	"testing"
)

func TestCase1(t *testing.T) {

	var (
		n        int  = 27
		expected bool = true
	)

	result := isPowerOfThree(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v , Result = %v", expected, result)
	}

}

func TestCase2(t *testing.T) {

	var (
		n        int  = 0
		expected bool = false
	)

	result := isPowerOfThree(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v , Result = %v", expected, result)
	}

}

func TestCase3(t *testing.T) {

	var (
		n        int  = 9
		expected bool = true
	)

	result := isPowerOfThree(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v , Result = %v", expected, result)
	}

}

func TestCase4(t *testing.T) {

	var (
		n        int  = 45
		expected bool = false
	)

	result := isPowerOfThree(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v , Result = %v", expected, result)
	}

}
