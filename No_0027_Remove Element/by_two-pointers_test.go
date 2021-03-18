package main

import (
	"testing"
)

func TestCase1( t *testing.T){

	var(
		nums = []int{3 , 2, 2, 3}
		val = 3
		expected = 2
	)

	result := removeElement(nums, val)
	if result != expected {
		t.Errorf("\n Wrong answer. result = %v. expected = %v", result, expected)
	}
}



func TestCase2( t *testing.T){

	var(
		nums = []int{0, 1, 2, 2, 3, 0, 4, 2}
		val = 2
		expected = 5
	)

	result := removeElement(nums, val)
	if result != expected {
		t.Errorf("\n Wrong answer. result = %v. expected = %v", result, expected)
	}
}