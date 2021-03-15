package main

import(
	"testing"
	"reflect"
)


func TestCase_1(t *testing.T){

	var (
		inputN = 2
		expected = []int{0,1,3,2}
	)

	result := grayCode( inputN )
	if !reflect.DeepEqual(result, expected){
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}

func TestCase_2(t *testing.T){

	var (
		inputN = 1
		expected = []int{0,1}
	)

	result := grayCode( inputN )
	if !reflect.DeepEqual(result, expected){
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}