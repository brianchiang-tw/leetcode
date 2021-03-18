package main

import (
	"math"
	"math/rand"
)

type Solution struct {
	X_Center float64
	Y_Center float64
	Radius   float64
}

func Constructor(radius, x_center, y_center float64) Solution {

	// Initialize random seed with system time
	rand.Seed(time.now().UnixNano())

	return Solution{Radius: radius, X_Center: x_center, Y_Center: y_center}
}

func (this *Solution) RandPoint() []float64 {

	// random theta from 0 to 2 * pi
	randTheta := rand.Float64() * 2 * math.Pi

	// random radius from 0 to R
	randRadius := math.Sqrt(rand.Float64()) * (this.Radius)

	// compute random point based on polar coordination
	randX_Coord := randRadius*math.Sin(randTheta) + this.X_Center
	randY_Coord := randRadius*math.Cos(randTheta) + this.Y_Center

	return []float64{randX_Coord, randY_Coord}
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(radius, x_center, y_center);
 * param_1 := obj.RandPoint();
 */

 
// Because this is a problem of randomness, therefore local testbench is not provided
