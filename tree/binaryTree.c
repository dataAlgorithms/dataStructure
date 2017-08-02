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



/*
Driver program

Output:
Preorder traversal of binary tree is
1 2 4 5 3
Inorder traversal of binary tree is
4 2 5 1 3
Postorder traversal of binary tree is
4 5 2 3 1
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

    return 0;
}
