package No_0423

import (
	"testing"
)

func TestCase1(t *testing.T){
	var(
		s string = "owoztneoer"
		expected string = "012"
	)

	result := originalDigits(s)

	if result != expected{
		t.Errorf("Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}



func TestCase2(t *testing.T){
	var(
		s string = "fviefuro"
		expected string = "45"
	)

	result := originalDigits(s)

	if result != expected{
		t.Errorf("Wrong answer. Expected = %v, Result = %v", expected, result)
	}
}