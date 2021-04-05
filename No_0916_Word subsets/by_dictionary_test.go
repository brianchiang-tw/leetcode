package No_0916

import (
	"testing"
)

func compare(src, target []string) bool {

	if len(src) != len(target) {
		return false
	}

	for idx, element := range src {
		if element != target[idx] {
			return false
		}
	}
	return true

}
func TestCase1(t *testing.T) {

	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"e", "o"}
	expected := []string{"facebook", "google", "leetcode"}

	result := wordSubsets(A, B)

	if !compare(result, expected) {
		t.Errorf("Wrong! Expected = %v, result = %v", expected, result)
	}
}

func TestCase2(t *testing.T) {

	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"l", "e"}
	expected := []string{"apple", "google", "leetcode"}

	result := wordSubsets(A, B)

	if !compare(result, expected) {
		t.Errorf("Wrong! Expected = %v, result = %v", expected, result)
	}
}

func TestCase3(t *testing.T) {

	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"e", "oo"}
	expected := []string{"facebook", "google"}

	result := wordSubsets(A, B)

	if !compare(result, expected) {
		t.Errorf("Wrong! Expected = %v, result = %v", expected, result)
	}
}

func TestCase4(t *testing.T) {

	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"lo", "eo"}
	expected := []string{"google", "leetcode"}

	result := wordSubsets(A, B)

	if !compare(result, expected) {
		t.Errorf("Wrong! Expected = %v, result = %v", expected, result)
	}
}

func TestCase5(t *testing.T) {

	A := []string{"amazon","apple","facebook","google","leetcode"}
	B := []string{"ec","oc","ceo"}
	expected := []string{"facebook","leetcode"}

	result := wordSubsets(A, B)

	if !compare(result, expected) {
		t.Errorf("Wrong! Expected = %v, result = %v", expected, result)
	}
}
