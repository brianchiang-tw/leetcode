package No_0032

import (
	"testing"
)

func TestCase1(t *testing.T){
	var (
		s string = "(()"
		expected int = 2
	)

	result := longestValidParentheses(s)

	if result != expected {
		t.Errorf("Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}



func TestCase2(t *testing.T){
	var (
		s string = ")()())"
		expected int = 4
	)

	result := longestValidParentheses(s)

	if result != expected {
		t.Errorf("Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}



func TestCase3(t *testing.T){
	var (
		s string = ""
		expected int = 0
	)

	result := longestValidParentheses(s)

	if result != expected {
		t.Errorf("Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}