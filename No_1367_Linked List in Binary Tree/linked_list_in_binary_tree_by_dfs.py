# This is just a practice to get the big picture of framework
# Not a good implementation in time complexity and space complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        def connect_sub_path( head: ListNode, root:TreeNode) -> bool:
        
            if head is None:
                return True

            if root is None:
                return False

            if head.val != root.val:
                return False
            
            else:
                return connect_sub_path( head.next, root.left ) or connect_sub_path(head.next, root.right)
            
        # ------------------------------
        
        if root is None:
            return False
            
        if head.val != root.val:
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        else:
            return connect_sub_path(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)



def test_bench():

    ## Test_case_#1
    root_1 = TreeNode(1)
    root_1.left = TreeNode(4)
    root_1.right = TreeNode(4)

    root_1.left.right = TreeNode(2)
    root_1.right.left = TreeNode(2)

    root_1.left.right.left = TreeNode(1)
    root_1.right.left.left = TreeNode(6)
    root_1.right.left.right = TreeNode(8)

    root_1.right.left.right.left = TreeNode(1)
    root_1.right.left.right.right = TreeNode(3)

    head_1 = ListNode(4)
    head_1.next = ListNode(2)
    head_1.next.next = ListNode(8)
    # expected output:
    '''
    True
    '''

    print( Solution().isSubPath(head = head_1, root = root_1) )



    ## Test_case_#2
    root_2 = TreeNode(1)
    root_2.left = TreeNode(4)
    root_2.right = TreeNode(4)

    root_2.left.right = TreeNode(2)
    root_2.right.left = TreeNode(2)

    root_2.left.right.left = TreeNode(1)
    root_2.right.left.left = TreeNode(6)
    root_2.right.left.right = TreeNode(8)

    root_2.right.left.right.left = TreeNode(1)
    root_2.right.left.right.right = TreeNode(3)

    head_2 = ListNode(1)
    head_2.next = ListNode(4)
    head_2.next.next = ListNode(2)
    head_2.next.next.next = ListNode(6)
    head_2.next.next.next.next = ListNode(8)
    # expected output:
    '''
    False
    '''

    print( Solution().isSubPath(head = head_2, root = root_2) )


    return



if __name__ == '__main__':

    test_bench()