package No_0377

import (
	"testing"
)

func TestCase1(t *testing.T){
	var(
		nums []int=[]int{1,2,3}
		target int = 4
		expected int = 7
	)

	result := combinationSum4(nums, target)

	if result != expected{
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v", expected, result)
	}

}


func TestCase2(t *testing.T){
	var(
		nums []int=[]int{9}
		target int = 3
		expected int = 0
	)

	result := combinationSum4(nums, target)

	if result != expected{
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v", expected, result)
	}

}