package main

import(
	"testing"
)

func TestCase1(t* testing.T){
	var(
		N = 1
		expected = true
	)

	result := reorderedPowerOf2( N )

	if result != expected{
		t.Errorf("\nresult = %v. expected = %v", result, expected)
	}

}

func TestCase2(t* testing.T){
	var(
		N = 10
		expected = false
	)

	result := reorderedPowerOf2( N )

	if result != expected{
		t.Errorf("\nresult = %v. expected = %v", result, expected)
	}

}

func TestCase3(t* testing.T){
	var(
		N = 16
		expected = true
	)

	result := reorderedPowerOf2( N )

	if result != expected{
		t.Errorf("\nresult = %v. expected = %v", result, expected)
	}

}

func TestCase4(t* testing.T){
	var(
		N = 24
		expected = false
	)

	result := reorderedPowerOf2( N )

	if result != expected{
		t.Errorf("\nresult = %v. expected = %v", result, expected)
	}

}

func TestCase5(t* testing.T){
	var(
		N = 46
		expected = true
	)

	result := reorderedPowerOf2( N )

	if result != expected{
		t.Errorf("\nresult = %v. expected = %v", result, expected)
	}

}