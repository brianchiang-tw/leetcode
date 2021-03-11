package main

import (
	"testing"
)

func TestCase1(t *testing.T) {

	var (
		coins    = []int{1, 2, 5}
		amount   = 11
		expected = 3
	)
	result := coinChange(coins, amount)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}



func TestCase2(t *testing.T) {
	var (
		coins    = []int{2}
		amount   = 3
		expected = -1
	)
	result := coinChange(coins, amount)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}


func TestCase3(t *testing.T) {
	var (
		coins    = []int{1}
		amount   = 0
		expected = 0
	)
	result := coinChange(coins, amount)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}


func TestCase4(t *testing.T) {
	var (
		coins    = []int{1}
		amount   = 1
		expected = 1
	)
	result := coinChange(coins, amount)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}


func TestCase5(t *testing.T) {
	var (
		coins    = []int{1}
		amount   = 2
		expected = 2
	)
	result := coinChange(coins, amount)
	if result != expected {
		t.Errorf("Running result = %v; \n expected = %v", result, expected)
	}
}