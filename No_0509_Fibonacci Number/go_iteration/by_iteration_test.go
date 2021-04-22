package No_0509

import (
	"testing"
)

func TestCase1(t *testing.T) {

	var (
		n        int = 0
		expected int = 0
	)

	result := fib(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v. \n", expected, result)
	}
}

func TestCase2(t *testing.T) {

	var (
		n        int = 1
		expected int = 1
	)

	result := fib(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v. \n", expected, result)
	}
}

func TestCase3(t *testing.T) {

	var (
		n        int = 2
		expected int = 1
	)

	result := fib(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v. \n", expected, result)
	}
}

func TestCase4(t *testing.T) {

	var (
		n        int = 3
		expected int = 2
	)

	result := fib(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v. \n", expected, result)
	}
}

func TestCase5(t *testing.T) {

	var (
		n        int = 4
		expected int = 3
	)

	result := fib(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v. \n", expected, result)
	}
}

func TestCase6(t *testing.T) {

	var (
		n        int = 5
		expected int = 5
	)

	result := fib(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v. \n", expected, result)
	}
}

func TestCase7(t *testing.T) {

	var (
		n        int = 10
		expected int = 55
	)

	result := fib(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v. \n", expected, result)
	}
}

func TestCase8(t *testing.T) {

	var (
		n        int = 30
		expected int = 832040
	)

	result := fib(n)

	if result != expected {
		t.Errorf("\n Wrong answer. Expected = %v, Result = %v. \n", expected, result)
	}
}
