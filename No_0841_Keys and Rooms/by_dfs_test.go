package main

import(
	"testing"
)

func TestCase1(t *testing.T){
	var(
		inputRooms = [][]int{{1}, {2}, {3}, {}}
		expected = true
	)

	result := canVisitAllRooms(inputRooms)

	if result != expected{
		t.Errorf("Wrong answer. result = %v . expected = %v", result, expected)
	}
}



func TestCase2(t *testing.T){
	var(
		inputRooms = [][]int{{1, 3}, {3, 0 , 1}, {2}, {0}}
		expected = false
	)

	result := canVisitAllRooms(inputRooms)

	if result != expected{
		t.Errorf("Wrong answer. result = %v . expected = %v", result, expected)
	}
}