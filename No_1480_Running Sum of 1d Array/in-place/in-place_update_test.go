package main

import (
	"fmt"
	"os"
	"reflect"
	"testing"
)

func TestCase1(t *testing.T) {

	var (
		input    = []int{1, 2, 3, 4}
		expected = []int{1, 3, 6, 10}
	)
	result := runningSum(input)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}

func TestCase2(t *testing.T) {

	var (
		input    = []int{1, 1, 1, 1, 1}
		expected = []int{1, 2, 3, 4, 5}
	)
	result := runningSum(input)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}



func TestCase3(t *testing.T) {

	var (
		input    = []int{3, 1, 2, 10, 1}
		expected = []int{3, 4, 6, 16, 17}
	)
	result := runningSum(input)
	if !reflect.DeepEqual(result, expected) {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}



func TestMain(m *testing.M) {

	fmt.Println("Testing start")
	exitValue := m.Run()
	fmt.Println("Testing finish")
	os.Exit(exitValue)
}