package No_1642

import (
	"container/heap"
)

// An IntHeap is a min-heap of integers
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	minElement := old[n-1]
	*h = old[0:n-1]
	return minElement
}

func furthestBuilding(heights []int, bricks int, ladders int) int {

	// min-heap to store building gaps
	buildingGapHeap := &IntHeap{}
	heap.Init(buildingGapHeap)

	totalBuildings := len(heights)

	// scan each building pair's gap
	for i := 0 ; i < totalBuildings-1 ; i++{

		curBuildingGap := heights[i+1] - heights[i]

		if curBuildingGap > 0 {

			// next building is higher than current one, add to min heap
			heap.Push( buildingGapHeap, curBuildingGap )
		}

		if buildingGapHeap.Len() > ladders{
			
			// the number of positive is more than the number of ladders
			// use bricks to fill the gap
			gapToClimb := heap.Pop( buildingGapHeap).(int)
			bricks -= gapToClimb
		}

		if bricks < 0 {

			// we can not fill more gaps, because the bricks is run out.
			return i
		}
	}


	return totalBuildings-1
}


// n : the number of heights
// k : the number of building gap

//// Time Complexity: O( n log k )
//
// The overhead in time is the cost of iteration, which is of O( n log k )

//// Space Complexity: O( k )
//
// The overhead in space is the storage for heap, which is of O( k )