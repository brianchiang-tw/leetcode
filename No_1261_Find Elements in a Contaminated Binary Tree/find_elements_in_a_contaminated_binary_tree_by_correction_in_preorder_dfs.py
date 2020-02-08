'''

Description:

Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
bool find(int target) Return if the target value exists in the recovered binary tree.
 

Example 1:



Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 



Example 2:



Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False



Example 3:



Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 10^4]
Total calls of find() is between [1, 10^4]
0 <= target <= 10^6

'''



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:

    def helper( self, node, correct_value ):
        
        # Base case:
        # Empty tree or empty node
        if not node:
            return

        # Correct current node
        # Update node value set
        node.val = correct_value
        self.node_value.add( correct_value )

        # Update next level with DFS
        self.helper( node.left, 2 * correct_value + 1)
        self.helper( node.right, 2 * correct_value + 2 )

    # -----------------------------------------
    
    
    def __init__(self, root: TreeNode):
        
        
        self.root = root

        # a set of node value in binary tree with given root
        self.node_value = set()
        
        # correct whole tree, from root node with correction value 0
        self.helper( self.root, 0 )
        

    def find(self, target: int) -> bool:
        
        # lookup target in node value set
        return (target in self.node_value)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)



# n : the number of nodes in binary tree
# q : the number of queries

## Time Compleity:
#
# in __init__():
# The overhed in time of __init__() is cost of the DFS traversal, which is of O( n ).
#
# in find():
# The overhead in time of find() is the cost of element looking up in set, which is of O( 1 ) * ( q ) = O( q )


## Space Complexity:
#
# in __init__():
# The overhead in space of __init() is the cost of set growing of node_value, which is of O( n ).
#
# in find()
# The overhhead in space of find() is the result array of output, which is of O( q ).



def test_bench():

    ## Test case_#1
    root_1 = TreeNode(-1)
    root_1.right = TreeNode(-1)

    test_data = [1,2]

    # expected output:
    '''
    [False, True]
    '''

    obj = FindElements(root_1)
    print( list( map( obj.find, test_data ) ) )



    ## Test case_#2
    root_2 = TreeNode(-1)
    root_2.left = TreeNode(-1)
    root_2.right = TreeNode(-1)

    root_2.left.left = TreeNode(-1)
    root_2.left.right = TreeNode(-1)

    test_data = [1,3,5]

    # expected output:
    '''
    [True, True, False]
    '''

    obj = FindElements(root_2)
    print( list( map( obj.find, test_data ) ) )

    return



if __name__ == '__main__':

    test_bench()