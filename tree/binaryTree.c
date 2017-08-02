#include <stdio.h>
#include <stdlib.h.>

struct binaryTreeNode
{
    int data;
    struct binaryTreeNode *left;
    struct binaryTreeNode *right;
};

void printPostorder(struct binaryTreeNode *node);
void printInorder(struct binaryTreeNode *node);
void printPreorder(struct binaryTreeNode *node);
void printLevelorder(struct binaryTreeNode *root);
void printGivenLevel(struct binaryTreeNode *root, int level);

/* 
 newTreeNode allocates a new node with the given data
 and NULL left and right pointers
*/
struct binaryTreeNode *newTreeNode(int data)
{
    // Allocate memory for new node
    struct binaryTreeNode *node = (struct binaryTreeNode*)malloc(sizeof(struct binaryTreeNode));

    // Assign data to the node
    node->data = data;

    // Initialize left and right children as NULL
    node->left = NULL;
    node->right = NULL;

    return node;
}

/*
 post order traversal of binary tree
*/
void printPostorder(struct binaryTreeNode *node)
{
    if (node == NULL)
        return;

    //first recur on left subtree
    printPostorder(node->left);

    //then recur on right subtree
    printPostorder(node->right);

    // deal with the node
    printf("%d ", node->data);
}

/*
 in order traversal of binary tree
*/
void printInorder(struct binaryTreeNode *node)
{
    if (node == NULL)
        return;

    //first recur on left subtree
    printInorder(node->left);

    //then deal with the node
    printf("%d ", node->data);

    //recur on right subtree
    printInorder(node->right);

}

/*
 pre order traversal of binary tree
*/
void printPreorder(struct binaryTreeNode *node)
{
    if (node == NULL)
        return;

    //deal with the node
    printf("%d ", node->data);

    //recur on left subtree
    printPreorder(node->left);

    //recur on right subtree
    printPreorder(node->right);


}

// print level order traversal a tree
void printLevelorder(struct binaryTreeNode *root)
{
    int h = height(root);
    int i;

    for (i=1; i<=h; i++)
        printGivenLevel(root, i);
}

// Print nodes at a given level
void printGivenLevel(struct binaryTreeNode *root, int level)
{
    if (root == NULL)
        return;

    if (level == 1)
        printf("%d ", root->data);
    else if (level > 1)
    {
        printGivenLevel(root->left, level-1);
        printGivenLevel(root->right, level-1);
    }
}

/* Compute the height of a tree -- the number of 
   nodes along the longest path from the root node
    down to the farthest leaf node*/
int height(struct binaryTreeNode *root)
{
    if (root == NULL)
        return 0;
    else 
    {
        // Compute the height of each subtree
        int lheight = height(root->left);
        int rheight = height(root->right);

        // Use the larger one
        if (lheight > rheight)
            return lheight+1;
        else
            return rheight+1;
    }
}

/*
Driver program

Output:
Preorder traversal of binary tree is
1 2 4 5 3
Inorder traversal of binary tree is
4 2 5 1 3
Postorder traversal of binary tree is
4 5 2 3 1
Levelorder traversal of binary tree is
1 2 3 4 5
*/
int main()
{
    // Create root
    struct binaryTreeNode *root = newTreeNode(1);
    root->left = newTreeNode(2);
    root->right = newTreeNode(3);

    root->left->left = newTreeNode(4);
    root->left->right = newTreeNode(5);
    /*
           1
       /       \
      2          3
    /   \       /  \
   4    5  NULL  NULL
  /  \
NULL NULL
*/

    printf("\nPreorder traversal of binary tree is \n");
    printPreorder(root);
 
    printf("\nInorder traversal of binary tree is \n");
    printInorder(root);  
 
    printf("\nPostorder traversal of binary tree is \n");
    printPostorder(root);

    printf("\nLevelorder traversal of binary tree is \n");
    printLevelorder(root);
    
    return 0;
}
