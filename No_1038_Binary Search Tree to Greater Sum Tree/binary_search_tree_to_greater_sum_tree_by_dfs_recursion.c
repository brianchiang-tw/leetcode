
#define NULL (void*) 0

//Definition for a binary tree node.
 struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
 

static int accumulation = 0;

struct TreeNode* helper(struct TreeNode* root){

    if ( root == NULL )
    {
        return NULL;
    }
    else
    {   
        helper( root->right );
        
        accumulation += root->val;
        root->val = accumulation;
        
        helper( root->left );
        
        return root;
    }
    
}


struct TreeNode* bstToGst(struct TreeNode* root){

    accumulation = 0;
    return helper(root);
}