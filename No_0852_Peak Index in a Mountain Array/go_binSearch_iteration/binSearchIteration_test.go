package main

import (
	"testing"
)

func TestCase_1(t *testing.T) {
	var (
		arr      = []int{0, 1, 0}
		expected = 1
	)

	result := peakIndexInMountainArray(arr)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}

func TestCase_2(t *testing.T) {
	var (
		arr      = []int{0, 2, 1, 0}
		expected = 1
	)

	result := peakIndexInMountainArray(arr)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}


func TestCase_3(t *testing.T){
	var (
		arr      = []int{0, 10, 5, 2}
		expected = 1
	)

	result := peakIndexInMountainArray(arr)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}	
}


func TestCase_4(t *testing.T){
	var (
		arr      = []int{3, 4, 5, 1}
		expected = 2
	)

	result := peakIndexInMountainArray(arr)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}	
}


func TestCase_5(t *testing.T){
	var (
		arr      = []int{24,69,100,99,79,78,67,36,26,19}
		expected = 2
	)

	result := peakIndexInMountainArray(arr)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}	
}