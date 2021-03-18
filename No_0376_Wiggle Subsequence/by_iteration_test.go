package main

import (
	"testing"
)

func TestCase1(t *testing.T){
	var(
		input = []int{1, 7, 4, 9, 2, 5}
		expected = 6
	)

	result := wiggleMaxLength( input )

	if result != expected {
		t.Errorf("\nresult = %v. expected = %v", result, expected)
	}

}



func TestCase2(t *testing.T){
	var(
		input = []int{1, 17, 5, 10, 13, 15, 10, 5, 16, 8}
		expected = 7
	)

	result := wiggleMaxLength( input )

	if result != expected {
		t.Errorf("\nresult = %v. expected = %v", result, expected)
	}

}



func TestCase3(t *testing.T){
	var(
		input = []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
		expected = 2
	)

	result := wiggleMaxLength( input )

	if result != expected {
		t.Errorf("\nresult = %v. expected = %v", result, expected)
	}

}