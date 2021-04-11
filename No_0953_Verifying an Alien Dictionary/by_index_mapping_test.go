package No_0953

import (
	"testing"
)

func TestCase1(t *testing.T) {
	var (
		words    []string = []string{"hello", "leetcode"}
		order    string   = "hlabcdefgijkmnopqrstuvwxyz"
		expected bool     = true
	)

	result := isAlienSorted(words, order)
	if result != expected {
		t.Errorf("\n Wrong answe. Expected = %v, Result = %v", expected, result)
	}
}

func TestCase2(t *testing.T) {
	var (
		words    []string = []string{"word", "world", "row"}
		order    string   = "worldabcefghijkmnpqstuvxyz"
		expected bool     = false
	)

	result := isAlienSorted(words, order)
	if result != expected {
		t.Errorf("\n Wrong answe. Expected = %v, Result = %v", expected, result)
	}
}

func TestCase3(t *testing.T) {
	var (
		words    []string = []string{"apple", "app"}
		order    string   = "abcdefghijklmnopqrstuvwxyz"
		expected bool     = false
	)

	result := isAlienSorted(words, order)
	if result != expected {
		t.Errorf("\n Wrong answe. Expected = %v, Result = %v", expected, result)
	}
}
