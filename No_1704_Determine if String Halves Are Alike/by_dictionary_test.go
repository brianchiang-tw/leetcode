package No_1704

import (
	"testing"
)

func TestCase1(t *testing.T){
	var (
		s string = "book"
		expected bool = true
	)

	result := halvesAreAlike(s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}

func TestCase2(t *testing.T){
	var (
		s string = "textbook"
		expected bool = false
	)

	result := halvesAreAlike(s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}

func TestCase3(t *testing.T){
	var (
		s string = "MerryChristmas"
		expected bool = false
	)

	result := halvesAreAlike(s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}

func TestCase4(t *testing.T){
	var (
		s string = "AbCdEfGh"
		expected bool = true
	)

	result := halvesAreAlike(s)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}