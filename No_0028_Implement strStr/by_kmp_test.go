package main

import (
	"testing"
)


func TestCase1(t* testing.T){
	var(
		haystack string="hello"
		needle string="ll"
		expected int=2
	)

	result := strStr(haystack, needle)

	if result != expected{
		t.Errorf("Wrong solution.\n result = %v, expected = %v", result, expected)
	}

}


func TestCase2(t *testing.T){
	var(
		haystack string="aaaaa"
		needle string="bba"
		expected int=-1
	)

	result := strStr(haystack, needle)

	if result != expected{
		t.Errorf("Wrong solution.\n result = %v, expected = %v", result, expected)
	}
}


func TestCase2(t *testing.T){
	var(
		haystack string=""
		needle string=""
		expected int=0
	)

	result := strStr(haystack, needle)

	if result != expected{
		t.Errorf("Wrong solution.\n result = %v, expected = %v", result, expected)
	}
}