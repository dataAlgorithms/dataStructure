struct BinaryTreeNode {
    int data;
    struct BinaryTreeNode *left;
    struct BinaryTreeNode *right;
};

/*
Visit the root
Traverse the left subtree in Preorder
Traverse the right subtree in Preorder


Time Complexity: O(n)
Space Complexity: O(n)
*/
void PreOrder(struct BinaryTreeNode *root) {
    if (root) {
        printf("%d", root->data);
        PreOrder(root->left);
        PreOrder(root->right);
    }
}

/*
In the recursive version, a stack is required as we need to remember the current node so that after
completing the left subtree we can go to the right subtree. To simulate the same, first we process the
current node and before going to the left subtree, we store the current node on stack. After completing the
left subtree processing, pop the element and go to its right subtree. Continue this process until stack is
nonempty.


Time Complexity: O(n)
Space Complexity: O(n)
*/

void PreOrderNonRecursive(struct BinaryTreeNode *root) {
    struct Stack *S = createStack();

    while (1) {
        while (root) {
            //Process current node
            printf("%d", root->data);

            push(S, root);

            //If left subtree exists, add to stack
            root = root->left;
        }

        if (isEmptyStack(S))
            brerak;

        root = pop(S);

        //Indicates completion of left subtree and current node, now to g to right subtree
        root = root->right;
    }

    deleteStack(S);
}
