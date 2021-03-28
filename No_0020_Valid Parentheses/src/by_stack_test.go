package No_0020

import (
	"testing"
)

func TestCase1(t *testing.T) {
	var (
		input_s  string = "()"
		expected bool   = true
	)

	result := isValid(input_s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v  Result = %v", expected, result)
	}
}

func TestCase2(t *testing.T) {
	var (
		input_s  string = "()[]{}"
		expected bool   = true
	)

	result := isValid(input_s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v  Result = %v", expected, result)
	}
}

func TestCase3(t *testing.T) {
	var (
		input_s  string = "(]"
		expected bool   = false
	)

	result := isValid(input_s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v  Result = %v", expected, result)
	}
}

func TestCase4(t *testing.T) {
	var (
		input_s  string = "([)]"
		expected bool   = false
	)

	result := isValid(input_s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v  Result = %v", expected, result)
	}
}

func TestCase5(t *testing.T) {
	var (
		input_s  string = "{[]}"
		expected bool   = true
	)

	result := isValid(input_s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v  Result = %v", expected, result)
	}
}
