package No_1074


import(
	"testing"
)

func TestCase1(t *testing.T){
	var(
		matrix [][]int = [][]int{{0, 1, 0}, {1, 1, 1}, {0, 1, 0}}
		target int = 0
		expected int = 4
	)

	result := numSubmatrixSumTarget(matrix, target)
	
	if result != expected {
		t.Errorf("\n Wrong answer. Expected =%v , Result =%v \n", expected, result)
	}

}

func TestCase2(t *testing.T){
	var(
		matrix [][]int = [][]int{{1, -1}, {-1, 1}}
		target int = 0
		expected int = 5
	)

	result := numSubmatrixSumTarget(matrix, target)
	
	if result != expected {
		t.Errorf("\n Wrong answer. Expected =%v , Result =%v \n", expected, result)
	}

}

func TestCase3(t *testing.T){
	var(
		matrix [][]int = [][]int{{904}}
		target int = 0
		expected int = 0
	)

	result := numSubmatrixSumTarget(matrix, target)
	
	if result != expected {
		t.Errorf("\n Wrong answer. Expected =%v , Result =%v \n", expected, result)
	}

}